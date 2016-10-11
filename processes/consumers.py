from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http

# Connected to websocket.connect
@channel_session_user_from_http
def ws_add(message):
    # Accept connection
    message.reply_channel.send({"accept": True})

    # Add them to the right group
    Group("chat-%s" % message.user.id).add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    Group("chat-%s" % message.user.id).send({
        "text": message['text'],
    })

# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("chat-%s" % message.user.id).discard(message.reply_channel)
