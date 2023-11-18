from .database import Database

class CourseSection():
    # implement crud operation here
    
    @staticmethod
    def createCourseSection(sectionId, courseId, classCapacity, instructorName):
        # print(cls.instance)
        value = Database.query(
            """
            INSERT INTO CourseSection(sectionId, courseId, classCapacity, instructorName)
            VALUES (%s,%s,%s,%s)
            """,
            (sectionId, courseId, classCapacity, instructorName),
            getID = True
            )
        return value
    
    pass