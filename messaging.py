from flask_socketio import Namespace, emit,send
import json
class Message(Namespace):
    def on_connect(self):
        print("here")

    def on_disconnect(self):
        print("there")

    def on_message(self, data):
        print("here")
        print(data)
        emit('message_received', json.dumps(data))