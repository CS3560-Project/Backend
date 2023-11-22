from .database import Database

class ClassServerDB:

    @staticmethod
    def createClassServer(serverName):
        print(serverName)
        value = Database.query("""
            INSERT INTO ClassServer(serverName)
            VALUES (%s)
        """,
        (serverName,),
        getID=True)
        return value

    @staticmethod
    def getClassServer(serverID):
        # print(serverID)
        
        # serverIDs = tuple(serverID.split(","))
        # print(serverIDs)
        value = Database.query(
            """
            SELECT * FROM ClassServer WHERE serverID in (%s);
            """,
            (serverID,),
            isDictionary=True,
            fetchVal=True
        )
        
        return value
    
    
        