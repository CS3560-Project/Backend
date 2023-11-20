from flask import jsonify, request, send_file, make_response
import io
import json
import os
from flask.views import MethodView, View
from database.channelDB import ChannelThe as Channel
from database.classServerDB import ClassServerDB
from utils.validator import validate_input
from Exceptions.apiExceptions import MissingArgumentException

class ChannelView(MethodView):

    def post(self):
        required_fields = ["channelName", "serverID"]
        data = json.loads(request.data.decode('utf-8'))

        try:
            validate_input(data.keys(), required_fields)
        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        try:
            channel_name = data["channelName"]
            server_id = data["serverID"]
        except KeyError as e:
            return jsonify({"error": f"Missing '{e.args[0]}' in data"}), 400

        new_channel = Channel.post_channel(channelName=channel_name, serverID=server_id)

        return jsonify({"success": "created", "channelID": new_channel}), 201

    def get(self):
        data = json.loads(request.data.decode('utf-8'))
        required_fields = ["channelId"]
        try:
            validate_input(data.keys(), required_fields)
        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        channel = Channel.get_channel(data["channelId"])

        if channel:
            return jsonify({
                "channelName": channel["channelName"],
                "channelID": channel["channelId"],
                "serverID": channel.get("serverID", None),  # Add serverID if present
                "serverName": ClassServerDB.getClassServer(channel.get("serverID", None))["serverName"]
            })
        else:
            return jsonify({"error": "Channel not found"}), 404



    def patch(self):
        data = json.loads(request.data.decode('utf-8'))
        required_fields = ["channelID", "newChannelName"]

        try:
            validate_input(data.keys(), required_fields)
        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        Channel.patch_channel_name(data["channelID"], data["newChannelName"])

        return jsonify(f"Channel {data['channelID']} name changed to {data['newChannelName']}"), 200

    def delete(self):
            data = json.loads(request.data.decode('utf-8'))
            required_fields = ["channelId"]
            try:
                validate_input(data.keys(), required_fields)


            except MissingArgumentException as e:
                return jsonify({"error": e.message}), e.error_code
            try:
                server_id = Channel.get_channel(data["channelId"])["serverID"]
                Channel.delete_channel(data["channelId"])
                return jsonify({"success": "deleted", "channelID": data["channelId"],"serverID:" : server_id, "serverName" : ClassServerDB.getClassServer(server_id)["serverName"] }), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500