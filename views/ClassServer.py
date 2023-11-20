from flask import jsonify, request
from flask.views import MethodView
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import MissingArgumentException
from database.classServerDB import ClassServerDB
from database.imageDB import Image
import os

class ClassServer(MethodView):
    def post(self):
        required_fields = ["serverName"]
        data = json.loads(request.data.decode('utf-8'))

        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code


        if "image" not in data.keys():
            with open(os.path.join(os.getcwd(),"image","userProfiles","download.jpg"),"rb") as file:
                image = file.read()
            
        else:
            #implement image here if they do put an image
            pass

        imageID = Image.store_image(image)

        server_id = ClassServerDB.createClassServer(data["serverName"], imageID)

        return jsonify({"success": "created", "serverID": server_id}), 201

    def get(self):

        data = json.loads(request.data.decode('utf-8'))
        server_name = request.args.get("serverName")

        try:
            validate_input([server_name], ["serverName"])

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        server = ClassServer.getClassServer(server_name)

        if server:
            return jsonify({"serverName": server.serverName, "serverID": server.serverID})
        else:
            return jsonify({"error": "ClassServer not found"}), 404