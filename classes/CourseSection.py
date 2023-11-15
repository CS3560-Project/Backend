from Course import Course

class CourseSection(Course):
    """
    A class to represent a course section


    Attribute roomNumber (int): The room number of the section

    Attribute instructorName (string): The name of the instructor of the section

    Attribute startTime (string): The start time of the section

    Attribute endTime (string): The end time of the section
    """

    def __init__(self, courseName="", courseId="", sectionId=0, roomNumber="", classCapacity=0, instructorName="") -> None:
        super().__init__(self, courseName, courseId)
        self._sectionId = sectionId
        self.roomNumber = roomNumber
        self.classCapacity = classCapacity
        self.instructorName = instructorName

    @property
    def classCapacity(self) -> int:
        """
        Returns instructor name
        """
        return self.classCapacity

    @classCapacity.setter
    def classCapacity(self, classCapacity: int) -> None:
        """
        Set section instructor name
        """
        self.classCapacity = classCapacity

    @property
    def instructorName(self) -> str:
        """
        Returns instructor name
        """
        return self.instructorName

    @instructorName.setter
    def instructorName(self, instructorName: str) -> None:
        """
        Set section instructor name
        """
        self.instructorName = instructorName

    def __str__(self) -> str:
        super.__str__()
        return f"Section Number:{self._sectionId}\nInstructor Name: {self.instructorName}"