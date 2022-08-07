# basic imports
from cgitb import text
import logging
import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# calendar import
from ics import Calendar, Event
# arrow import (for time)
import arrow

#### TODO ARROW TIME CONVERSION ####


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

    # calendar maker
    calendar_maker(say, text, client, channel)

# event - app direct message
@app.event("message")
def message_handler(say, message, client):
    # Intro message
    say("~=~ CalendarBot! ~=~")

    # extracting text + channel
    text = message["text"]
    channel = message["channel"]

    # calendar maker
    calendar_maker(say, text, client, channel)

#############################################################################################

# calendar making function
def calendar_maker(say, text, client, channel):
    # checking text format
    if text.count("\"") == 8: # if text has 6 ("" - double quotes)
        text = text[text.find("\""):]
    elif text.find("help") != -1: # if text has help
        say("~=~ Help ~=~")
        say("~=~ Format: ~=~")
        say("~=~ \"<title>\" \"<description>\" \"<start time>\" \"<end time>\" ~=~")
        say("~=~ Example: ~=~")
        say("~=~ \"My cool event\" \"This is a cool event\" \"2022-08-06 22:00:00\" \"2022-08-07 10:00:00\" ~=~")
        say("~=~ Help ~=~")
        return
    else: # if text doesn't have the correct format
        say("~=~ Sorry, I don't understand the inputted format ~=~")
        return

    #splitting text into sub-parts, removing unessary dividers
    subtexts = text.split("\"")
    subtexts.pop(0)
    subtexts.pop(1)
    subtexts.pop(-1)
    subtexts.pop(-2)

    ###test - printing subtexts###
    print(subtexts)

    # initiation message
    say("~=~ Making Event! ~=~")
    


    ### TODO CREATE FILE ###

    ### ARROW CONVERSION ###

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