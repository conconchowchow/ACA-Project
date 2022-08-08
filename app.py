#############################################################################################

# Name: CalendarBot
# Description: Bot that can create calendar files on Slack workspace
# Author: Connor Chow
# Date: 2022-08-07
# Notes: For ACA 2022

#############################################################################################

# basic imports
from cgitb import text
from datetime import tzinfo
import logging
import os
from time import time

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# calendar import
from ics import Calendar, Event
# arrow and timezone import (for time)
import arrow
from dateutil import tz

# slack app setup + config
logging.basicConfig(level=logging.INFO)
load_dotenv()
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
app = App(token=SLACK_BOT_TOKEN)

#############################################################################################

# event - app mention from channel
@app.event("app_mention")
def mention_handler(say, event, client):
    # Intro message
    say("~=~ CalendarBot! ~=~")

    # extracting text + channel
    text = event["text"]
    channel = event["channel"]
    user_id = event["user"]

    # calendar maker
    calendar_maker(say, text, client, channel, user_id)

# event - app direct message
@app.event("message")
def message_handler(say, message, client):
    # Intro message
    say("~=~ CalendarBot! ~=~")

    # extracting text + channel
    text = message["text"]
    channel = message["channel"]
    user_id = message["user"]

    # calendar maker
    calendar_maker(say, text, client, channel, user_id)

#############################################################################################

# calendar making function
def calendar_maker(say, text, client, channel, user_id):
    # checking text format
    if text.count("\"") == 8: # if text has 6 ("" - double quotes)
        text = text[text.find("\""):]
    elif text.find("help") != -1: # if text has help
        say("~=~ Help ~=~")
        say("~=~ Format: ~=~")
        say("~=~ \"<title>\" \"<description>\" \"<start time>\" \"<end time>\" ~=~")
        say("~=~ Example: ~=~")
        say("~=~ \"My cool event\" \"This is a cool event\" \"2022-08-06 22:00:00\" \"2022-08-07 10:00:00\" ~=~")
        say("~=~ Note: ~=~")
        say("~=~ 1. Dates must be in the format YYYY-MM-DD HH:MM:SS ~=~")
        say("~=~ 2. Times must be inputted based on a 24-hour time/clock ~=~")
        say("~=~ 3. Timezone is based on the user sending the message! ~=~")
        say("~=~ Help ~=~")
        return
    else: # if text doesn't have the correct format
        say("~=~ Sorry, I don't understand the inputted format ~=~")
        return

    # splitting text into sub-parts, removing unessary dividers
    subtexts = text.split("\"")
    subtexts.pop(0)
    subtexts.pop(1)
    subtexts.pop(2)
    subtexts.pop(-1)
    subtexts.pop(-2)
    ###test - printing subtexts
    # print("<testing> subtexts: ")
    # print(subtexts)

    # extracting user's timezones
    user_data = client.users_info(user = user_id)
    timezone = user_data["user"]["tz"]
    ###test - printing user's timezones###
    # print("<testing> timezone: ")
    # print(timezone)


    #taking times in subtext and converting to arrow (to make the correct timezones in .ics file)
    start_arrow = arrow.get(subtexts[2], 'YYYY-MM-DD HH:mm:ss')
    end_arrow = arrow.get(subtexts[3], 'YYYY-MM-DD HH:mm:ss')
    start_arrow = start_arrow.replace(tzinfo = timezone)
    end_arrow = end_arrow.replace(tzinfo = timezone)
    ###test - printing arrow times###
    print("<testing> start time after convert: ")
    print(start_arrow)
    print("<testing> end time after convert: ")
    print(end_arrow)

    # creating calendar/event
    say("~=~ Making Event! ~=~")
    c = Calendar()
    e = Event()
    # adding event details
    e.name = subtexts[0]
    e.description = subtexts[1]
    e.begin = start_arrow
    e.end = end_arrow
    # e.begin = subtexts[2] # taking raw data from subtexts
    # e.end = subtexts[3] # taking raw data from subtexts
    c.events.add(e)
    ###test - printing calendar/event###
    # print("<testing> event: ")
    # print(c.events) # print event # {<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>}

    # creating ics file
    with open('event.ics', 'w') as f:
        f.writelines(c.serialize_iter())    

    # file upload
    filename = "./event.ics"
    client.files_upload(
        channels = channel,
        file = filename,
        initial_comment = "~=~ Here is your calendar file: ~=~",
    )

#############################################################################################

# main method/function
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()