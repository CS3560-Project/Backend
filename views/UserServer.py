from flask import jsonify, request
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
import json
from database.userServerDB import UserServer as US
from database.courseSectionDB import CourseSection
class UserServer(MethodView):
    def post(self):
        required_field = ["userID","courseName","sectionID"]
        data = json.loads(request.data.decode("utf-8"))

        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            return jsonify({"error":e.message}),e.error_code
        serverID = CourseSection.getCourseSection(data["courseName"],data["sectionID"])
        US.createUserServer(serverID,data.get("userID"))
        return jsonify({"status":"created"}),200
        
