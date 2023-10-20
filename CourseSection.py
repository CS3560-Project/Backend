class CourseSection:
    """
    A class to represent a course section


    Attribute roomNumber (int): The room number of the section

    Attribute instructorName (string): The name of the instructor of the section

    Attribute startTime (string): The start time of the section

    Attribute endTime (string): The end time of the section
    """
    # HIDDEN ATTRIBUTES
    # _sectionId (int): Unique section id
    # _courseId (int): Associated course id

    def __init__(self, roomNumber=0, instructorName="", startTime="", endTime="") -> None:
        self._sectionId = 0
        self._courseId = 0
        self.roomNumber = roomNumber
        self.instructorName = instructorName
        self.startTime = startTime
        self.endTime = endTime

    @property
    def roomNumber(self):
        """
        Returns room information class based on room number
        """
        return self._roomNumber

    @roomNumber.setter
    def roomNumber(self, roomNumber: int) -> None:
        """
        Set section room number
        """

        self._roomNumber = roomNumber

    @property
    def instructorName(self) -> str:
        """
        Returns instructor name
        """
        return self._instructorName

    @instructorName.setter
    def instructorName(self, instructorName: str) -> None:
        """
        Set section instructor name
        """
        self._instructorName = instructorName

    @property
    def startTime(self) -> str:
        """
        Returns section start time
        """
        return self._startTime

    @startTime.setter
    def startTime(self, startTime: str) -> None:
        """
        Set section start time
        """
        self._startTime = startTime

    @property
    def endTime(self) -> str:
        """
        Returns section end time
        """
        return self._endTime

    @endTime.setter
    def endTime(self, endTime: str) -> None:
        """
        Set section end time
        """
        self._endTime = endTime

    def __str__(self) -> str:
        return f"Room Number: {self.roomNumber}\nInstructor Name: {self.instructorName}\nStart Time: {self.startTime}\nEnd Time: {self.endTime}"
