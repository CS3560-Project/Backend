#branch creation
from Message import Message
class Channel:
    def __init__(self,channelName = "",channelID = 0):
        self.__channelID:int = channelID
        self.channelName:str = channelName  
    @property
    def channelName(self) -> str:
        # returns the channel's name
        return self.channelName
    @channelName.setter
    def channelName(self, channelName:str):
        self.channelName:str = channelName


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