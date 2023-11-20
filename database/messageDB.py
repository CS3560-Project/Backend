from .database import Database

class Message():
    @staticmethod 
    def create_message(channelID, serverID, userID, timeSent,message,images = None):
        Database.query(
            """
            INSERT INTO Message(channelId,serverID,userID,timeSent,message)
            VALUES(%s,%s,%s,%s)
            """,
            (channelID,serverID,userID,timeSent),
            getID = True


        )
        # test these 
        for image in images:

            Database.query(
                """
                """
            )