from flask import jsonify, request
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from database.ClassServer import ClassServer 

class ClassServer(MethodView):

    def post(self):
        # get the data from the request
        required_fields = ["serverName"]
        
        data = json.loads(request.data.decode('utf-8'))
        
        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            
            return jsonify({"error": e.message}), e.error_code
        
        # create a new ClassServer
        server_name = data["serverName"]
        server_profile_picture = b''

        # Call the createClassServer method
        server_id = ClassServer.createClassServer(server_name, server_profile_picture)
        


        return jsonify({"success": "created", "serverID": server_id}), 201
