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
    def getClassServer(serverIDs):
        placeholders = ', '.join(['%s'] * len(serverIDs))
        sql = f"SELECT * FROM ClassServer WHERE serverID IN ({placeholders})"
        values = Database.query(sql, list(serverIDs), isDictionary=True, fetchVal=True)
        return values
    
    
        