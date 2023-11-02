from flask import Flask, jsonify,request
from database import Database
from flask.views import MethodView

from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


Database.getInstance()

class Account(MethodView):
    
    
    def post(self):
        # get the data from 
        data = request.data
        print(data)
        return jsonify("test")
    def get(self):
        # global database
        
        data = request.args
        
        return jsonify(data)

acc = Account.as_view('acc')
app.add_url_rule('/main/', view_func = acc)
