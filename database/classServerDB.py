from .database import Database

class ClassServerDB:

    @staticmethod
    def createClassServer(serverName, imageID):
        value = Database.query("""
            INSERT INTO ClassServer (serverName, imageID)
            VALUES (%s, %s);
        """,
        (serverName, imageID),
        getID=True)
        return value

    @staticmethod
    def getClassServer(serverID):
        value = Database.query(
            """
            SELECT * FROM ClassServer WHERE serverID = %s;
            """,
            (serverID,),
            isDictionary=True,
            fetchVal=True
        )
        print(type(value[0]))
        print(value)
        return value[0]
