from flask_socketio import Namespace, emit
from database.messageDB import Message as messageDB
import json 
class Message(Namespace):
    def on_connect(self):
        print("here")

    def on_disconnect(self):
        pass

    def on_message(self, data):
        userID = data.get("id")
        userName = data.get("sender")
        messsage = data.get("text")
        time = data.get("timestamp")
        image = data.get("image") 
        channelID = data.get("channelID") #still waiting on this
        serverID = data.get("serverID") # still waiting
        # print(userID)
        messageID = messageDB.create_message(
            channelID,serverID,userID,time,messsage,image
        )
        data["messageID"] = messageID
        
        emit('message_received', json.dumps(data))

