from cgitb import text
import logging
import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)

### command example(not used by my bot) ###
# # This will match any message that contains 👋
# @app.message(":wave:")
# def say_hello(message, say):
#     user = message['user']
#     say(f"Hi there, <@{user}>!")
#
# @app.command("/hello-socket-mode")
# def hello_command(ack, body):
#     user_id = body["user_id"]
#     ack(f"Hi, <@{user_id}>!")
    
### example function head - def message_handler(body, context, payload, options, say, event): ###

@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    print(body)
    # text = body["text"]
    # say(text)
    calendarMaker(say)

@app.event("message")
def message_handler(message, body, context, payload, options, say, event):
    text = message["text"]
    say(text)
    calendarMaker(say)
    # pass

def calendarMaker(say):
    say("Hello World!!")

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()