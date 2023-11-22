from .database import Database
from .imageDB import Image
class Message():
    @staticmethod 
    def create_message(channelID, serverID, userID, timeSent,message,image = None):
        
        messageID = Database.query(
            """
            INSERT INTO Message(userID,timeSent,message)
            VALUES(%s,%s,%s)
            """,
            (userID,timeSent,message),
            getID = True
        )
        
        Database.query(
            """
            INSERT INTO SERVERMESSAGE(ChannelID,ServerID,MessageID)
            VALUES(%s,%s,%s)

            """,
            (channelID,serverID,messageID)
        )
        # test these 
        if image:
            imageID = imageDB.store_image(image)
            Database.query(
                """
                INSERT INTO MessageImage(imageID,messageID)
                VALUES(%s,%s)
                """,
                (imageID,messageID)
            )
        return messageID
    @staticmethod
    def delete_message(messageID):
        Database.query(
            """
            DELETE FROM MESSAGE:
            where messageID = %s,
            """,
            (messageID,)
        )
    @staticmethod
    def get_messages_for_channel(channelID):
        # test this
        messages = Database.query(
            """
                SELECT * FROM message where messageID in (
                    SELECT messageID FROM ServerMessage where channelID = %s
                )
            """,
            (channelID,),
            fetchVal = True,
            isDictionary = True
            )
        return messages
