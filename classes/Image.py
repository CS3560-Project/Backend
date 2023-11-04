from .database import Database
class Image:
    '''
    A class to represent the Image 

    Attribute image (PIL.Image.Image): The image that after being processed

    Attribute size (int): The size, in bytes, of the image

    Attribute length (int): The length (pixels) of the image

    Attribute width (int): The width, (pixels), of the image
    '''
    def __init__(self,imageLink="",size = 2048, length = 10,width =10):
        self.image:bytes =  PIL.Image.open(imageLink) # fix this later
        self.type:str = size
        self.length:int = length
        self.width:int = width
        
        

    