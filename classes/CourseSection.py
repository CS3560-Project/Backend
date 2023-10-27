class CourseSection(Course):
    """
    A class to represent a course section


    Attribute roomNumber (int): The room number of the section

    Attribute instructorName (string): The name of the instructor of the section

    Attribute startTime (string): The start time of the section

    Attribute endTime (string): The end time of the section
    """

    def __init__(self, courseName="", courseId=0, sectionId=0, roomNumber=0, classCapacity=0, instructorName="", startTime="", endTime="") -> None:
        super().__init__(self, courseName, courseId)
        self._sectionId = sectionId
        self.roomNumber = roomNumber
        self.classCapacity = classCapacity
        self.instructorName = instructorName
        self.startTime = startTime
        self.endTime = endTime

    @property
    def roomNumber(self):
        """
        Returns room information class based on room number
        """
        return self.roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int) -> None:
        """
        Set section room number
        """
        self.roomNumber = roomNumber

    @property
    def classCapacity(self) -> int:
        """
        Returns instructor name
        """
        return self.classCapacity

    @classCapacity.setter
    def instructorName(self, instructorName: str) -> None:
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

    @property
    def startTime(self) -> str:
        """
        Returns section start time
        """
        return self.startTime

    @startTime.setter
    def startTime(self, startTime: str) -> None:
        """
        Set section start time
        """
        self.startTime = startTime

    @property
    def endTime(self) -> str:
        """
        Returns section end time
        """
        return self.endTime

    @endTime.setter
    def endTime(self, endTime: str) -> None:
        """
        Set section end time
        """
        self.endTime = endTime

    def __str__(self) -> str:
        super.__str__()
        return f"Room Number: {self.roomNumber}\nInstructor Name: {self.instructorName}\nStart Time: {self.startTime}\nEnd Time: {self.endTime}"