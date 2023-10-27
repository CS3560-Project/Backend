import Image.Image
import User.User
class Message:

    """
    A class to represent a Message section


    Attribute message (str): The contents of the message

    Attribute sender (User): The user in which who sent the message

    Attribute sentDate (string): the date in which the message was sent/edited

    Attribute images (list[Image]):  a list of qall iamges aassociated witht he message

    Attribute edited(bool): an indicator of whether or not a message has been edited 
    """
    # HIDDEN ATTRIBUTES
    # __messageID(int) : an identifier for the message

    def __init__(self,messageId,message,sender,sentDate,channelID,images):
        self.__messageID:int = messageID
        self.message:str = message
        self.sender:User = sender
        self.channelID:int = channelID
        self.images:list[Image] = images
        self.edited:bool = False
        self.sentDate:str = sentDate
        
    @property
    def message(self)-> str:
        # returns the message 
        return self.message
    @message.setter
    def message(self,message:str):
        # changes a specific message
        self.message = message
    @property
    def sender(self)->User:
        # returns the user who sent the message
        # a seter method is not needded as the user will never change
        return self.sender
    @property
    def channelID(self)->int:
        # returns the channelID in which the message was sent in
        # a setter method is not needed as the channelID will stay constant
        return self.channelID

    @property
    def images(self)->list[Image]:
        # returns  the images associated with a message
        return self.images
    @images.setter
    def images(self,images:list[Image]):
        # updagtes the message's image to be the new images
        self.images = images
    @property
    def edited(self)->bool:
        # returns whether or not the message has been edited
        return self.edited
    @edited.setter
    def edited(self,status:bool,date:str):
        # updates whether or not the message has been edited alongside the edited date
        # since the only time the sentdate should be edited is when it's edited, there won't be
        # a setter for sentDate
        self.sentDate = date
        self.edited = status
    @property
    def sentDate(self)->str:
        # returns the date the message was sent
        return self.sentDate
    
    
        

class MessageImage:
    '''
    A class that bridges a user with a message. 
    This class' only purpose is to make sure the message has access to the images
    
    messageID(int) the ID that is associated with the message
    
    image(Image) the image that we want associated witht the image
    '''

    def __init__(self,messageID,image):
        self.messageID:int = messageID
        self.image:Image = image
        