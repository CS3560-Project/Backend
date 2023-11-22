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
from views.Course import Course

from flask_cors import CORS

import json

load_dotenv()
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins='*',debug = True)
CORS(app)



"""
post: takes ina username,password,email (and profilePicture is optional) and returns the userID
get : takes in a email and password and returns userID,userName,password,imageID,serverIDs
get: if instead only a userID is passed, username,passowrd,imageID and a list of serverIDs(not implemented yet)


delete : takes an email and deletes it 
"""
app.add_url_rule('/account/', view_func = Account.as_view('acc'))

app.add_url_rule('/image/',view_func = Image.as_view('image'))



"""
post: takes in a  channelName and serverID and creates a channel in the specified server (channel ID is returned)
get: takes ina  serverID and channelID and returns the channelName,channelID, serverID and serverName
patch: takes in a channelID and a newChannelName and changes the name of the specified channel
delete: takes ina  channelID and deletes it
"""
app.add_url_rule('/channel/',view_func = ChannelView.as_view('channel'))


"""
classServer
post: take an server name and spits out a server with  3 channels predefined
import thing to note is it returns the serverID which shoudl be stored
get: takes a serverID and rerieves the serverNaame,ID all channels and all users associated wit it
"""
app.add_url_rule('/classserver/',view_func = ClassServer.as_view('classserver'))

# use this get endpoint to get all messages associated witha  sepcifc channel oif a server
app.add_url_rule('/message/',view_func = Message_endpoint.as_view('message'))

# use this post endpoint to join users with servers
app.add_url_rule('/userServer/',view_func = UserServer.as_view('userServer'))

# important to note that userID,channelID and serverID cannot be null
socketio.on_namespace(Message("/message"))


# use this post endpoint to join users with servers
app.add_url_rule('/course/',view_func = Course.as_view('course'))

app.add_url_rule("/courseSection",view_func = CourseSection.as_view("courseSection"))
