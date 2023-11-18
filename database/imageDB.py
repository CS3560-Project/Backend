from .database import Database
from PIL import Image as Img
from io import BytesIO
class Image:
    # implement crud operation here
    @staticmethod
    def store_image(img):
        img_byte = BytesIO(img)
        img_type = Img.open(img_byte).format
        
        imageID = Database.query(
            """
                INSERT INTO IMAGE(image,imageType)

                VALUES(%s,%s)
            """,
            (img,img_type),
            getID = True
            )
        return imageID

    @staticmethod
    def get_image(ID):
        image = Database.query(
            """
            SELECT * FROM IMAGE
            WHERE imageID = %s
            LIMIT 1
            """,
            (ID,),
            fetchVal = True
        
        )
        return image
        