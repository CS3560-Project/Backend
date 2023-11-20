from flask import jsonify,request,make_response,send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from database.userDB import User
from database.imageDB import Image
import os
class Account(MethodView):
    
    
    def post(self):
        # get the data from 
        
        required_field = ["username","password","email"]
        
        data = json.loads(request.data.decode('utf-8'))
        
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            
            return jsonify({"error":e.message}),e.error_code
        if data["profilePicture"] == "":
            with open(os.path.join(os.getcwd(),"image","userProfiles","download.jpg"),"rb") as file:
                image = file.read()
            
        else:
            #implement image here if they do put an image
            image = data["profilePicture"]
            pass
        imageID = Image.store_image(image)

        userID = User.createAccount(data["username"],data["email"],data["password"],imageID )
        
        print(userID)
        return {"userID":userID},201
    def get(self):
        data = request.args.get("email")
        # implement a check on required arguments (when using validator function make sure is_body  is false to ensure correct error is sent)
        db_val = User.getAccount(email=data)[0]
        
        
        return jsonify({
            "userID":db_val["userID"],
            "userName":db_val["userName"],
            "password":db_val["password"],
            "imageID":db_val["profilePictureID"]
        })
        
    def patch(self):
        # changes the account
        data = json.loads(request.data.decode('utf-8'))
        required_field = ["email","username","password"]
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            
            return jsonify({"error":e.message}),e.error_code
        User.changeAccount(data.get("email"),data.get("username"),data.get("password"))
        
        return jsonify(f"{data.get('email')} changed"),200
       
    def delete(self):
            email = request.args.get("email")
            User.deteleteAccount(email=email)
            return jsonify("account deleted")
