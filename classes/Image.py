from PIL import Image as PILImage
from .database import Database

class Image:
    '''
    A class to represent the Image 

    Attribute image (PIL.Image.Image): The image that after being processed

    Attribute size (int): The size, in bytes, of the image

    Attribute length (int): The length (pixels) of the image

    Attribute width (int): The width, (pixels), of the image
    '''
    def __init__(self, imageLink="", size=2048, length=10, width=10):
        self._image: PILImage.Image = PILImage.open(imageLink)  # Assuming imageLink is a valid file path
        self._size: int = size
        self._length: int = length
        self._width: int = width
        
        Database.query(
            """
            CREATE TABLE IF NOT EXISTS Image(
                imageID INT PRIMARY KEY AUTO_INCREMENT,
                imageType VARCHAR(255)
            )
            """
        )

    @property
    def image(self) -> PILImage.Image:
        return self._image
    
    @property
    def size(self) -> int:
        return self._size
    
    @property
    def length(self) -> int:
        return self._length
    
    @property
    def width(self) -> int:
        return self._width

    @size.setter
    def size(self, size: int) -> None:
        # Add custom validation logic if needed
        self._size = size

    @length.setter
    def length(self, length: int) -> None:
        # Add custom validation logic if needed
        self._length = length

    @width.setter
    def width(self, width: int) -> None:
        # Add custom validation logic if needed
        self._width = width
