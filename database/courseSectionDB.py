from .database import Database

class CourseSection():
    # implement crud operation here
    
    @staticmethod
    def createCourseSection(courseName, sectionId, serverID):
        # print(cls.instance)
        value = Database.query(
            """
            INSERT INTO CourseSection(courseName, sectionId,serverID)
            VALUES (%s,%s,%s)
            """,
            (courseName, sectionId,serverID),
            
            )
        
    
    @staticmethod
    def getCourseSection(courseName, sectionId):
        value = Database.query(
            """
            SELECT serverID FROM CourseSection where courseName = %s AND sectionId = %s;
            """,
            (courseName, sectionId),
            
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