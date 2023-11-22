from flask import jsonify,request,make_response,send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView
from database.channelDB import ChannelThe as Channel
from database.courseSectionDB import CourseSection as Section
from database.courseDB import Course
from database.classServerDB import ClassServerDB
import os

class CourseSection(MethodView):
    def post(self):

        required_field = ["courseName", "sectionId", ]

        data = json.loads(request.data.decode('utf-8'))
        
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            return jsonify({"error":e.message}),e.error_code
        exists = Section.getCourseSection(data["courseName"],data["sectionId"])
        if len(exists) == 0:
            server_id = ClassServerDB.createClassServer(f'{data["courseName"]}-{data["sectionId"]}')
        
            courseSection = Section.createCourseSection(data["courseName"], data["sectionId"],server_id)
            general_id = Channel.post_channel(channelName="general",serverID=server_id)
            homework_id = Channel.post_channel(channelName="homework",serverID=server_id)
            offtopic_id = Channel.post_channel(channelName="offtopic",serverID=server_id)
        
            response_data = {
                "success": "created",
                "serverID": server_id,
                "serverName": f'{data["courseName"]}-{data["sectionId"]}',
                "defaultChannels": {
                    "general": Channel.get_channel(general_id),
                    "homework": Channel.get_channel(homework_id),
                    "offtopic": Channel.get_channel(offtopic_id)
                }
            }
            return jsonify(response_data),201
        else:
            return jsonify({"serverID":exists[0][0]})


    def get(self):
        course = request.args.get("courseName")
        section = request.args.get("sectionId")
        db_val = Section.getCourseSection(COURSE=course, sectionId=section)[0]


        return jsonify({
            "courseId":db_val["courseId"],
            "sectionId":db_val["sectionId"],
            
        })

    def delete(self):
        course = request.args.get("courseId")
        section = request.args.get("sectionId")
        Section.deleteCourseSection(courseId=course, sectionId=section)
        return jsonify("Course section deleted")


    