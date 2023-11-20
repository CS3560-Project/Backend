from pdb import run
from flask import jsonify, request, send_file
import io
import json
import os
from flask.views import MethodView
from database.channelDB import Channel, Channeldb
from utils.validator import validate_input
from Exceptions.apiExceptions import MissingArgumentException

class Channel(MethodView):
    def post(self):
        required_fields = ["channelName"]
        data = json.loads(request.data.decode('utf-8'))

        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        channel = Channel(channelName=data["channelName"])
        channel_id = Channeldb.post_channel(channel)

        return jsonify({"success": f"Channel '{data['channelName']}' created with ID {channel_id}"}), 201

    def get(self):
        channel_id = request.args.get("channelID")
        
        try:
            validate_input([channel_id], ["channelID"])
        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        channel = Channeldb.get_channel(channel_id)

        if channel:
            return jsonify({"channelName": channel.get_channel_name, "channelID": channel.channelID})
        else:
            return jsonify({"error": "Channel not found"}), 404

    def patch(self):
        data = json.loads(request.data.decode('utf-8'))
        required_fields = ["channelID", "newChannelName"]

        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        Channeldb.patch_channel_name(data["channelID"], data["newChannelName"])

        return jsonify(f"Channel {data['channelID']} name changed to {data['newChannelName']}"), 200