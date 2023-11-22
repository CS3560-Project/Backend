import json
from flask import jsonify, request
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
from database.courseDB import Course as CourseDB
from PIL import Image as Img


class Course(MethodView):
    
    def get(self):
        courseName = request.args.get("courseName")
        data = CourseDB.get_course_sections(courseName)
        print(data)

        return "hi", 200
