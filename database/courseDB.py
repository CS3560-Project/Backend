from .database import Database

class Course():
    # implement crud operation here

    @staticmethod
    def createCourse(courseId, courseName):
        # print(cls.instance)
        value = Database.query(
            """
            INSERT INTO Course(courseId, courseName)
            VALUES (%s,%s)
            """,
            (courseId, courseName),
            getID = True
            )
        return value

    pass