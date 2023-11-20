from .database import Database

class CourseSection():
    # implement crud operation here
    
    @staticmethod
    def createCourseSection(courseId, sectionId, classCapacity, instructorName):
        # print(cls.instance)
        value = Database.query(
            """
            INSERT INTO CourseSection(courseId, sectionId, classCapacity, instructorName)
            VALUES (%s,%s,%s,%s)
            """,
            (courseId, sectionId, classCapacity, instructorName),
            getID = True
            )
        return value
    
    @staticmethod
    def getCourseSection(courseId="", sectionId = 0):
        value = Database.query(
            """
            SELECT * FROM CourseSection where courseId = %s AND sectionId = %s;
            """,
            (courseId, sectionId),
            isDictionary=True,
            fetchVal = True
        )
        return value
    
    @staticmethod
    def deleteCourseSection(courseId="", sectionId = 0):
        Database.query(
            """
            DELETE FROM CourseSection where courseId = %s AND sectionId = %s;
            """,
            (courseId, sectionId)
        )


    pass