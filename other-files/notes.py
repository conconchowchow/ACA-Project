###### NOTES / SAMPLE CODE TO REFERENCE ######

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