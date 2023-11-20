from flask import Flask, jsonify,request
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os
from views.Account import Account
from views.Image import Image
from views.CourseSection import CourseSection

from flask_cors import CORS
import json

load_dotenv()
app = Flask(__name__)
socket = SocketIO(app, cors_allowed_origins="*")
CORS(app)


@socket.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})

@socket.on('message')
def handle_message(message):
    print(message)
    emit('message_received', json.dumps(message))

app.add_url_rule('/account/', view_func = Account.as_view('acc'))
app.add_url_rule('/image/',view_func = Image.as_view('image'))
app.add_url_rule('/section/',view_func = CourseSection.as_view('section'))