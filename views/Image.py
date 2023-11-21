from flask import jsonify, request
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
from database import imageDB
from PIL import Image as Img


class Image(MethodView):
    def post(self):
        photo_byte = request.data
        imageID = imageDB.Image.store_image(photo_byte)
        return jsonify({"imageID": imageID}), 200

    def get(self):
        photoID = request.args.get("imageID")
        data = imageDB.Image.get_image(photoID)[0]
        image=data[1]

        return jsonify({"image": image}), 200
