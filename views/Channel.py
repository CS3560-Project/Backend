from flask import jsonify,request
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from Message import Message
from database.channelDB import Channel  # Assuming you have a channel database module

class ChannelView(MethodView):

    def post(self):
        # get the data from the request
        required_fields = ["channelName"]
        
        data = json.loads(request.data.decode('utf-8'))
        
        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            
            return jsonify({"error": e.message}), e.error_code
        

        return jsonify({"success": "created", "channelID": channel.channelID}), 201
