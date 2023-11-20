from Message import Message

class Channel:
    """ 
    A class to represent a channel
    
    Attributes:
    channelName (str): The name of the channel
    """

    def __init__(self, channelName="") -> None:
        self.__channelName: str = channelName

    @property
    def channel_name(self) -> str:
        """Returns the channel's name"""
        return self.__channelName

    @channel_name.setter
    def channel_name(self, new_channel_name: str):
        """Sets the channel's name"""
        self.__channelName = new_channel_name



class ChannelMessage:
    '''
    A class that bridges a user channel with messages. 
    This class' only purpose is to make sure the channel and the message are linked

    messageID(int): the messages' ID number 
    channelID(int): the channel's ID number
    '''
    
    def __init__(self,messageID,channelID):
        self.messageID = messageID
        self.channelID= channelID