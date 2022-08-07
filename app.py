# basic imports
from cgitb import text
import logging
import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# calendar import
from ics import Calendar, Event

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
    # extracting text + channel
    text = event["text"]
    channel = event["channel"]

    # calendar maker
    calendarMaker(say, text, client, channel)

# event - app direct message
@app.event("message")
def message_handler(say, message, client):

    text = message["text"]
    channel = message["channel"]

    # calendar maker
    calendarMaker(say, text, client, channel)

#############################################################################################

# calendar making function
def calendarMaker(say, text, client, channel):
    # initiation message
    say("~=~ Calendar Bot! ~=~")

    # file upload
    filename = "./event.ics"
    client.files_upload(
        channels = channel,
        file = filename,
        initial_comment = "Here is your calendar file:",
    )

#############################################################################################

# main method/function
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()