from flask import jsonify,request,make_response,send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
import base64
from database.userDB import User
from database.imageDB import Image
from database.imageDB import Image
import os
class Account(MethodView):
    
    
    def post(self):
        # get the data from 
        
        required_field = ["username","password","email"]
        # data = request.files
        data = json.loads(request.data.decode("utf-8"))
        # print(data.get("file  "))
        

        
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            
            return jsonify({"error":e.message}),e.error_code
        if "profile" not in data.keys():
            with open(os.path.join(os.getcwd(),"image","userProfiles","download.jpg"),"rb") as file:
                image = file.read()

                
                
                
        else:
            image = base64.b64decode(data["profile"])
            
        
        imageID = Image.store_image(image)

        userID = User.createAccount(data["username"],data["email"],data["password"],imageID )
        

        return jsonify({"userID":userID}),201
        return jsonify({"userID":userID}),201
    def get(self):
        data = request.args.get("email")
        # implement a check on required arguments (when using validator function make sure is_body  is false to ensure correct error is sent)
        
        db_val = User.getAccount(email=data)
        if len(db_val) == 0 :
            return jsonify({"error": f"no account associated with {data}"}),404
        db_val = db_val[0]
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
