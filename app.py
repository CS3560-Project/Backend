from flask import Flask, jsonify,request
from database import userDB
from flask.views import MethodView
from dotenv import load_dotenv
import os
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
load_dotenv()

app = Flask(__name__)




class Account(MethodView):
    
    
    def post(self):
        # get the data from 
        required_field = ["username","password","email"]
        
        data = json.loads(request.data.decode('utf-8'))
        try:
            validate_input(data.keys(), required_field)
        except MissingArgumentException as e:
            
            return jsonify({"error":e.message}),e.error_code
        

        return jsonify({"success":"created"}),201
        # how are we sending status code
    def get(self):
        # global database
        
        data = request.args
        
        return jsonify(data)

acc = Account.as_view('acc')
app.add_url_rule('/main/', view_func = acc)
