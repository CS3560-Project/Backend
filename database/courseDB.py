from .database import Database


class Course:
    @staticmethod
    def create_course(course_name):

        Database.query("""
            INSERT INTO Course(courseName)
            VALUES(%s)
        """, (course_name,), getID=True)

    # Given: course_name, section_id
    # if course name exists, add section to course
    # else, create course and add section to course
    # 


    @staticmethod
    def get_course_sections(course_name):
        course = Database.query("""
            SELECT * FROM Course WHERE courseName = %s LIMIT 1
        """, (course_name,),
            fetchVal=True, isDictionary=True)
        courseId = course[0]["courseId"]

        return Database.query("""
            SELECT * FROM CourseSection WHERE courseId = %s
        """, (courseId,), isDictionary=True)
