class User:     # A class to represent a user
    """ 
    Attributes:

    userId (int): The unique ID of the user
    userName (str): The user's username
    email (str): The user's email
    [HIDDEN] _password (str): The password to the user's account
    """

    def __init__(self, userName="", email="", password="") -> None:
        
        self.userName = userName
        self.email = email
        self.password = password

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

class UserServer:
    """Attributes:
    userId (int): The unique ID of the user
    serverId (int): The unique ID of the server
    """

    def __init__(self, userId=0, serverId=0) -> None:
        self.userId = userId
        self.serverId = serverId

    @userId.setter
    def userId(self, userId) -> None:
        """
        Set a user's unique ID
        """
        self.userId = userId

    @serverId.setter
    def serverId(self, serverId) -> None:
        """
        Set a servers's unique ID
        """
        self.serverId = serverId

    @property
    def userId(self):
        """
        Return a user's unique id
        """
        return self.userId

    @property
    def serverId(self):
        """
        Set a server's unique ID
        """
        return self.serverId



