from .database import Database

class UserServer:

    @staticmethod
    def createUserServer(serverId, userId):
        value = Database.query(
            """
            INSERT INTO UserServers(serverID, userID)
            VALUES (%s,%s)
            """,
            (serverId, userId),
            getID = True
            )
        return value
    
    @staticmethod
    def getUserServer(userId):
        value = Database.query(
            """
            SELECT * FROM UserServers where userID = %s;
            """,
            (userId,),
            fetchVal = True
        )
        return value