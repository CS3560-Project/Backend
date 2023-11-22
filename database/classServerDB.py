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
        serverPlaceholders = ', '.join(['%s'] * len(serverIDs))
        allServers = Database.query(f"SELECT * FROM ClassServer WHERE serverID IN ({serverPlaceholders})", list(
            serverIDs), isDictionary=True, fetchVal=True)
        return allServers
