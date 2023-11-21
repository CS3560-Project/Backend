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
    def getUserOfServer(serverID):
        value = Database.query(
            """
            SELECT userID FROM UserServers where serverID = %s;
            """,
            (serverID,),
            fetchVal = True
        )
        return value

        
    @staticmethod
    def getServerIDS(userID):
        serverIDs = Database.query(
            """
                SELECT ServerID FROM UserServers where 
                userID = %s
            """,
            (userID,),
            fetchVal = True
        )
        return serverIDs

    
