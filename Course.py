class Course:
    """
    A class to represent a course section


    Attribute name (str): The name of the course
    Attribute courseID (int): The ID of the course
    Attribute classCapacity (int): The capacity the class can hold


    """
    # HIDDEN ATTRIBUTES
    # _courseId (int): Associated course id

    def __init__(self, name="", classCapacity=0) -> None:
        self.name = name
        self.courseId = 0
        self.classCapacity = classCapacity

    @property
    def name(self) -> str:
        """
        Returns the name of the course
        """
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of the course
        """
        self.name = name
    
    @property
    def courseID(self) -> str:
        """
        Returns the name of the course
        """
        return self.name

    @name.setter
    def courseID(self, courseID: str) -> None:
        """
        Sets the name of the course
        """
        self.courseID = courseID

    @property
    def classCapacity(self):
        """
        Returns class capacity
        """
        return self.classCapacity

    @classCapacity.setter
    def classCapacity(self, classCapacity: int) -> None:
        """
        Set class capacity
        """
        self.classCapacity = classCapacity


    def __str__(self) -> str:
        return f"Name: {self.name}\nCourse ID: {self.courseId}\nClass capacity: {self.classCapacity}\n"
