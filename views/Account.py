from flask import jsonify, request, make_response, send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
import base64
from database.userDB import User
from database.imageDB import Image
from database.userServerDB import UserServer
import os

class Account(MethodView):

    def post(self):
        required_field = ["username", "password", "email"]
        data = json.loads(request.data.decode("utf-8"))

        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:

            return jsonify({"error": e.message}), e.error_code
        if "profilePicture" not in data.keys() or data["profilePicture"] == "":
            with open(os.path.join(os.getcwd(), "image", "userProfiles", "download.jpg"), "rb") as file:
                image = file.read()
                image = "data:image/jpeg;base64," + base64.b64encode(image).decode('ASCII')
                # Converts local image to base64 string 

        else:
            image = data["profilePicture"]

        imageID = Image.store_image(image)

        userID = User.createAccount(
            data["username"], data["email"], data["password"], imageID)

        return jsonify({"userID": userID}), 200

    def get(self):
        email = request.args.get("email")
        password = request.args.get("password")
        # implement a check on required arguments (when using validator function make sure is_body  is false to ensure correct error is sent)

        db_val = User.getAccount(email=email)
        if len(db_val) == 0:
            return jsonify({"error": f"no account associated with {email}"}), 404
        db_val = db_val[0]
        if password != db_val["password"]:
            return jsonify({"error": "incorrect password"}), 404
        
        userServers = UserServer.getServerIDS(db_val["userID"])
        userServers = [x[0] for x in userServers]
        return jsonify({
            "userID": db_val["userID"],
            "userName": db_val["userName"],
            "password": db_val["password"],
            "imageID": db_val["profilePictureID"],
            "serverIDs":userServers
        }), 200

    def patch(self):
        # changes the account
        data = json.loads(request.data.decode('utf-8'))
        required_field = ["userID","email", "username", "password"]
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:

            return jsonify({"error": e.message}), e.error_code
        User.changeAccount(data.get("email"), data.get(
            "username"), data.get("password"))

        return jsonify(f"{data.get('email')} changed"), 200

    def delete(self):
        email = request.args.get("email")
        User.deteleteAccount(email=email)
        return jsonify("account deleted")
