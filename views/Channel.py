from flask import jsonify,request
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from database.userDB import User
import os
class Channel(MethodView):
    
    
    def post(self):
        # gets the data from body
        data = json.loads(request.data.decode('utf-8'))
        

        return jsonify("implement post endpoint for channel"),501
    def get(self):
        data = request.args.get("email")
        # implement a check on required arguments (when using validator function make sure is_body  is false to ensure correct error is sent)
        print(data)
        return jsonify("implement Channel get endpoint")
    def patch(self):
        data = json.loads(request.data.decode('utf-8'))
        # impelemt a check onr equired argeuments
        return jsonify("implement Channel set endpoint")
    
       