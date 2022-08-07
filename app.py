# basic imports
from cgitb import text
import logging
import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# calendar import
from ics import Calendar, Event


logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def mention_handler(say, event, client):
    text = event["text"]
    channel = event["channel"]
    calendarMaker(say, text, client, channel)

@app.event("message")
def message_handler(say, message, client):
    text = message["text"]
    channel = message["channel"]
    calendarMaker(say, text, client, channel)

def calendarMaker(say, text, client, channel):
    say("~=~ Calendar Bot! ~=~")

    filename = "./event.ics"

    client.files_upload(
        channels = channel,
        file = filename,
        initial_comment = "Here is your calendar file:",
    )

# Main
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()