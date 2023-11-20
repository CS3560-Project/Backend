from .database import Database

class ClassServerDB:

    @staticmethod
    def createClassServer(serverName, imageID):
        query = """
            INSERT INTO ClassServer (serverName, imageID)
            VALUES (%s, %s);
        """
        values = (serverName, imageID)

        server_id = Database.query(query, values)

        return server_id

    @staticmethod
    def getClassServer(serverName):
        server_info = Database.query(
            """
            SELECT * FROM ClassServer WHERE serverName = %s;
            """,
            (serverName,),
            fetchVal=True
        )

        return server_info