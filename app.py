from flask import Flask, jsonify,request
from flask_socketio import Namespace
from dotenv import load_dotenv
import os
from views.Account import Account
from views.Channel import ChannelView
from views.ClassServer import ClassServer
from views.Image import Image
from sockets.message import Message
from flask_socketio import SocketIO
from views.CourseSection import CourseSection
from views.Message import Message_endpoint
from views.UserServer import UserServer
from flask_cors import CORS

import json

load_dotenv()
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins='*',debug = True)
CORS(app)




app.add_url_rule('/account/', view_func = Account.as_view('acc'))
app.add_url_rule('/image/',view_func = Image.as_view('image'))

socketio.on_namespace(Message("/message"))


app.add_url_rule('/channel/',view_func = ChannelView.as_view('channel'))
app.add_url_rule('/classserver/',view_func = ClassServer.as_view('classserver'))
app.add_url_rule('/message/',view_func = Message_endpoint.as_view('message'))

app.add_url_rule('/userServer/',view_func = UserServer.as_view('userServer'))