from flask import jsonify, request
from flask.views import MethodView
from database.ClassServer import ClassServer
from Exceptions.apiExceptions import MissingArgumentException

class ClassServerView(MethodView):
    def post(self):
        required_fields = ["serverName"]
        data = json.loads(request.data.decode('utf-8'))

        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        server_name = data["serverName"]
        server_profile_picture = b''

        server_id = ClassServer.createClassServer(server_name, server_profile_picture)

        return jsonify({"success": "created", "serverID": server_id}), 201

    def get(self):
        server_name = request.args.get("serverName")

        try:
            validate_input([server_name], ["serverName"])

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        server = ClassServer.getClassServer(server_name)

        if server:
            return jsonify({"serverName": server.serverName, "serverID": server.serverID})
        else:
            return jsonify({"error": "ClassServer not found"}), 404
