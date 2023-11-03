class Course:
    """
    A class to represent a course

    Attribute courseName (str): The courseName of the course
    Attribute courseID (int): The ID of the course

    """

    def __init__(self, courseName="", courseId=0) -> None:
        self.courseName = courseName
        self.courseId = courseId

    @property
    def courseName(self) -> str:
        """
        Returns the name of the course
        """
        return self.courseName

    @courseName.setter
    def courseName(self, courseName: str) -> None:
        """
        Sets the name of the course
        """
        self.courseName = courseName

    @property
    def courseId(self) -> int:
        """ 
        Returns the ID of the course
        """
        return self.courseId
    @courseId.setter
    def courseId(self, courseId: int) -> int:
        """
        Returns the ID of the course
        """
        self.courseId = courseId

    def __str__(self) -> str:
        return f"Name: {self.courseName}\nCourse ID: {self._courseId}\n"
