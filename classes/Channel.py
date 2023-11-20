from Message import Message

class Channel:
    """ 
    A class to represent a channel
    
    Attributes:
    channelName (str): The name of the channel
    serverID (int): The ID of the server
    """

    def __init__(self, channelName="", serverID=None) -> None:
        self.__channelName: str = channelName
        self.__serverID: int = serverID

    @property
    def channel_name(self) -> str:
        """Returns the channel's name"""
        return self.__channelName

    @channel_name.setter
    def channel_name(self, new_channel_name: str):
        """Sets the channel's name"""
        self.__channelName = new_channel_name

    @property
    def server_id(self) -> int:
        """Returns the server's ID"""
        return self.__serverID

    @server_id.setter
    def server_id(self, new_server_id: int):
        """Sets the server's ID"""
        self.__serverID = new_server_id

class ChannelMessage:
    '''
    A class that bridges a user channel with messages. 
    This class' only purpose is to make sure the channel and the message are linked

    messageID (int): the messages' ID number 
    channelID (int): the channel's ID number
    serverID (int): the server's ID number
    '''
    
    def __init__(self, messageID, channelID, serverID):
        self.messageID = messageID
        self.channelID = channelID
        self.serverID = serverID
