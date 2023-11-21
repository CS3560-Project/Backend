from flask import jsonify, request
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
from database.messageDB import Message

class Message_endpoint(MethodView):
    def get(self):
        channelID = request.args.get("channelID")
        serverID = request.args.get("serverID")
        messages = Message.get_messages_for_channel(channelID,serverID)

        return messages


