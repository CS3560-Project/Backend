from .database import Database
from .database import imageDB
class Message():
    @staticmethod 
    def create_message(channelID, serverID, userID, timeSent,message,images = []):
        messageID = Database.query(
            """
            INSERT INTO Message(channelId,serverID,userID,timeSent,message)
            VALUES(%s,%s,%s,%s)
            """,
            (channelID,serverID,userID,timeSent),
            getID = True
        )
        # test these 
        for image in images:
            imageID = imageDB.store_image(image)
            Database.query(
                """
                INSERT INTO MessageImage(imageID,messageID)
                VALUES(%s,%s)
                """,
                (imageID,messageID)
            )
    @staticmethod
    def delete_message(messageID):
        Database.query(
            """
            DELETE FROM MESSAGE:
            where messageID = %s,
            """
            (messageID,)
        )
    @staticmethod
    def get_messages_for_channel(channelID,serverID):
        Database.query(
            """
                SELECT * FROM 
            """
            )
