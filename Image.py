import PIL
class Image:
    """
    
    """
    def __init__(self,imageLink="",size = 2048, length = 10,width =10):
        self.image:PIL.Image.Image =  PIL.Image.open(imageLink) 
        self.size:int = size
        self.length:int = length
        self.width:int = width
    