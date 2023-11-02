from Image import Image
from .database import Database


class ClassServer:
    '''
    A class to represent a ClassServer 

    Attribute serverName (str): The string value of the displayed name for the server

    Attribute profilePicture (Image): The image being displayed onto the server
    '''
    # Hidden Attributes
    # serverID(int): an identifier for which server
    

    def __init__(self, serverID = 0, serverName ="",profilePicture = None):
        data = Database.getInstance()
        # self.__serverID:int =serverID
        # self.serverName:str = serverName
        # self.profilePicture:Image  = profilePicture
        data.query(
            """CREATE TABLE IF NOT EXIST(
                serverID INT NOT NULL AUTO_INCREMENT,
                serverName varchar(255) NOT NULL,
                serverProfilePicture BLOB NOT NULL,
                PRIMARY KEY (serverID),
            )"""
            )
    
    @property
    def serverName(self) -> str:
        '''
        returns the name of the Server
        '''
        return self.serverName
    @serverName.setter
    def serverName(self,serverName:str):
        '''
        changes the attribute of the profilePicture
        '''
        self.serverName = serverName
    @property
    def profilePicture(self)-> Image:
        '''
        returns the profile picture of the channel
        '''
        return self.profilePicture
    @profilePicture.setter
    def profilePicture(self,profilePicture:Image):
        '''
        changes the value of the attribute profielPicture
        '''
        self.profilePicture = profilePicture

