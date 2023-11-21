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
        channel_id = request.args.get("channelId")

        if not channel_id:
            return jsonify({"error": "Missing required parameter 'channelId'"}), 400

        try:
            channel = Channel.get_channel(channel_id)
            if channel:
                server_id = channel.get("serverID", None)
                server_name = ClassServerDB.getClassServer(server_id)["serverName"] if server_id else None

                return jsonify({
                    "channelName": channel["channelName"],
                    "channelID": channel["channelId"],
                    "serverID": server_id,
                    "serverName": server_name
                })
            else:
                return jsonify({"error": "Channel not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500



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
        # Assuming "channelId" is a required query parameter
        channel_id = request.args.get("channelId")

        if not channel_id:
            return jsonify({"error": "Missing required parameter 'channelId'"}), 400

        try:
            server_id = Channel.get_channel(channel_id)["serverID"]
            Channel.delete_channel(channel_id)
            return jsonify({
                "success": "deleted",
                "channelID": channel_id,
                "serverID": server_id,
                "serverName": ClassServerDB.getClassServer(server_id)["serverName"]
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
