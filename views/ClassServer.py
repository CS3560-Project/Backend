from flask import jsonify, request
from flask.views import MethodView
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import MissingArgumentException
from database.classServerDB import ClassServerDB
from database.imageDB import Image
from database.channelDB import ChannelThe as Channel
import os

class ClassServer(MethodView):
    def post(self):

        required_fields = ["serverName"]

        data = json.loads(request.data.decode('utf-8'))

        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code
        
        
        
        
        
        server_id = ClassServerDB.createClassServer(data["serverName"])
        
        
        general_id = Channel.post_channel(channelName="general",serverID=server_id)
        homework_id = Channel.post_channel(channelName="homework",serverID=server_id)
        offtopic_id = Channel.post_channel(channelName="offtopic",serverID=server_id)



        response_data = {
            "success": "created",
            "serverID": server_id,
            "serverName": data["serverName"],
            "defaultChannels": {
                "general": Channel.get_channel(general_id),
                "homework": Channel.get_channel(homework_id),
                "offtopic": Channel.get_channel(offtopic_id)
            }
            }
        

        return jsonify(response_data), 201

    def get(self):

        # Assuming "serverID" is a required query parameter
        server_id = request.args.get("serverID")

        if not server_id:
            return jsonify({"error": "Missing required parameter 'serverID'"}), 400

        server = ClassServerDB.getClassServer(server_id)

        if server:
            all_channels = Channel.get_channel_from_server(server["serverID"])
            
            return jsonify({
                "serverName": server["serverName"],
                "serverID": server["serverID"],
                "channels": all_channels
            })
        else:
            return jsonify({"error": "ClassServer not found"}), 404
