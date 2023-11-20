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
        print(data)
        print("\n\n\n")
   

        if "imageID" not in data:
            print("not in data")
            print("\n\n\n")
            with open(os.path.join(os.getcwd(),"image","userProfiles","download.jpg"),"rb") as file:
                image = file.read()
            
        else:
            image = data["imageID"]
            pass
    
        
        print("\n\n\n")
        imageID = Image.store_image(image)
        print(imageID)
        
        print("\n\n\n")
        server_id = ClassServerDB.createClassServer(data["serverName"], imageID)
        
        
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

        data = json.loads(request.data.decode('utf-8'))
        required_fields = ["serverID"]

        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        server = ClassServerDB.getClassServer(data["serverID"])

        if server:
            all_channels = Channel.get_channel_from_server(server["serverID"])


            return jsonify({
                "serverName": server["serverName"],
                "serverID": server["serverID"],
                "channels": all_channels
            })
        else:
            return jsonify({"error": "ClassServer not found"}), 404