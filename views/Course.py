import json
from flask import jsonify, request
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
from database.courseDB import Course as CourseDB
from PIL import Image as Img


class Course(MethodView):
    def post(self):
        required_fields = ["courseName"]

        data = json.loads(request.data.decode('utf-8'))

        try:
            validate_input(data.keys(), required_fields)

        except MissingArgumentException as e:
            return jsonify({"error": e.message}), e.error_code

        CourseDB.create_course(data["courseName"])
        return jsonify({"success": "created"}), 200


    def get(self):
        courseName = request.args.get("courseName")
        data = CourseDB.get_course_sections(courseName)
        print(data)

        return "hi", 200
