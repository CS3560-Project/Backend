from flask import jsonify,request,make_response,send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from database.courseSectionDB import CourseSection
from database.courseDB import Course
import os

"""
GET
POST
DELETE
"""

"""
sectionId
courseId
classCapacity
instructorName
"""

class Message(MethodView):
    def post(self):

        required_field = ["courseId", "sectionId", "classCapacity", "instructorName"]

        data = json.loads(request.data.decode('utf-8'))
        
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            return jsonify({"error":e.message}),e.error_code
        
        courseSection = CourseSection.createCourseSection(data["courseId"], data["sectionId"], data["classCapacity"], data["instructorName"])
        

        return jsonify({"courseSection":courseSection}),201


    #def get(self):


    #def delete(self):


    