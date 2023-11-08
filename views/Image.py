from flask import jsonify,request
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

# class Image(MethodView):
#     def post(self):
#         data = json.loads(request.data.decode('utf-8'))
#         required_field = []
#         try