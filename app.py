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
def mention_handler(body, context, payload, options, say, event):
    text = event["text"]
    calendarMaker(say, text)

@app.event("message")
def message_handler(message, body, context, payload, options, say, event):
    text = message["text"]
    calendarMaker(say, text)

def calendarMaker(say, text):
    say(text)
    say("Hello World!!")


# Main
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()