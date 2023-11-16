from .database import Database

class Image:
    # implement crud operation here
    @staticmethod
    def store_image(img,image_type):
        Database.query(
            """
                INSERT INTO IMAGE(image,imageType)

                VALUES(%s,%s)
            """,
            (img,image_type)
            )

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
        