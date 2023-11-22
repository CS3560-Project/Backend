from flask import jsonify,request,make_response,send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from database.courseSectionDB import CourseSection as Section
from database.courseDB import Course
import os

class CourseSection(MethodView):
    def post(self):

        required_field = ["courseId", "sectionId", "classCapacity", "instructorName"]

        data = json.loads(request.data.decode('utf-8'))
        
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            return jsonify({"error":e.message}),e.error_code
        
        courseSection = Section.createCourseSection(data["courseId"], data["sectionId"], data["classCapacity"], data["instructorName"])
        

        return jsonify({"courseSection":courseSection}),201


    def get(self):
        course = request.args.get("courseName")
        section = request.args.get("sectionId")
        db_val = Section.getCourseSection(COURSE=course, sectionId=section)[0]


        return jsonify({
            "courseId":db_val["courseId"],
            "sectionId":db_val["sectionId"],
            "classCapacity":db_val["classCapacity"],
            "instructorName":db_val["instructorName"]
        })

    def delete(self):
        course = request.args.get("courseId")
        section = request.args.get("sectionId")
        Section.deleteCourseSection(courseId=course, sectionId=section)
        return jsonify("Course section deleted")


    