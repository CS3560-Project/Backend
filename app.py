from flask import Flask, jsonify,request
from flask_socketio import Namespace
from dotenv import load_dotenv
import os
from views.Account import Account
from views.Image import Image
from sockets.message import Message
from flask_socketio import SocketIO
from views.CourseSection import CourseSection
from flask_cors import CORS

import json

load_dotenv()
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins='*',debug = True)
CORS(app)




app.add_url_rule('/account/', view_func = Account.as_view('acc'))
app.add_url_rule('/image/',view_func = Image.as_view('image'))

socketio.on_namespace(Message("/message"))

