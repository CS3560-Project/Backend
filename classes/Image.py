import PIL
class Image:
    '''
    A class to represent the Image 

    Attribute image (PIL.Image.Image): The image that after being processed

    Attribute size (int): The size, in bytes, of the image

    Attribute length (int): The length (pixels) of the image

    Attribute width (int): The width, (pixels), of the image
    '''
    def __init__(self,imageLink="",size = 2048, length = 10,width =10):
        self.image:PIL.Image.Image =  PIL.Image.open(imageLink) 
        self.size:int = size
        self.length:int = length
        self.width:int = width
    