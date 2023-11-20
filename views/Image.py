from flask import jsonify,request,send_file
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
from database import imageDB
from io import BytesIO
from PIL import Image as Img

class Image(MethodView):
    def post(self):
        photo_byte = request.data
        
        
        
        imageID = imageDB.Image.store_image(photo_byte)
        return jsonify({"imageID":imageID}),201
    def get(self):
        # make error handler for thewse
        photoID = request.args.get("imageID")
        data = imageDB.Image.get_image(photoID)[0]
        image = data[1]
        image_type = data[2]
        
        return send_file(
            BytesIO(image),
            mimetype = f"/{image_type}"
        )
        



    