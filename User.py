class User:     # A class to represent a user
    """ 
    Attributes:

    userId (int): The unique ID of the user
    userName (str): The user's username
    email (str): The user's email
    [HIDDEN] _password (str): The password to the user's account
    """

    def __init__(self, userId=0, userName="", email="", _password="") -> None:
        self.userId = userId
        self.userName = userName
        self.email = email
        self._password = _password

    def userId(self, userId) -> None:
        # Sets a user's unique ID
        self.userId = userId

    def userId(self) -> int:
        # Returns a user's unique ID
        return self.userId

    def userName(self, userName) -> None:
        # Sets a user's username
        self.userName = userName

    def userName(self) -> str:
        # Returns a user's username
        return self.userName

    def email(self, email) -> None:
        # Sets a user's email
        self.email = email

    def email(self) -> str:
        # Returns a user's email
        return self.email

    def setPassword(self, password) -> None:
        # Sets a user's password
        self._password = password

