class CourseSection:
    """
    A class to represent a course section


    Attribute roomNumber (int): The room number of the section
    """
    # HIDDEN ATTRIBUTES
    # _courseId (int): Associated course id

    def __init__(self, name="", classCapacity=0) -> None:
        self.name = name
        self._courseId = 0
        self.classCapacity = classCapacity

    @property
    def name(self) -> str:
        """
        Returns the name of the course
        """
        return self._name

    @startTime.setter
    def name(self, name: str) -> None:
        """
        Sets the name of the course
        """
        self._name = name

    @property
    def classCapacity(self):
        """
        Returns class capacity
        """
        return self.classCapacity

    @roomNumber.setter
    def classCapacity(self, roomNumber: int) -> None:
        """
        Set class capacity
        """

        self.classCapacity = classCapacity


    def __str__(self) -> str:
        return f"Name: {self.name}\nCourse ID: {self._courseId}\nClass capacity: {self.classCapacity}\n"
