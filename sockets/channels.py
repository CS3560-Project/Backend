from flask_socketio import Namespace, emit
import json 
class Channel(Namespace):
    def on_connect(self):
        print("here")

    def on_disconnect(self):
        pass

    def on_message(self, data):
        print(data)
        emit('message_received', json.dumps(data))

