from flask import jsonify,request,make_response,send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from database.messageDB import Message
from database.channelDB import Channel
from database.imageDB import Image
from database.userDB import User

"""
GET
POST
PATCH
DELETE
"""

"""
messageId
message
sender
dateSent
edited
channelId
images
"""

class Message(MethodView):
    def post(self):


    def get(self):


    def patch(self):


    def delete(self):


    