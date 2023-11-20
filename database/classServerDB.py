from .database import Database

class ClassServer:

    @staticmethod
    def createClassServer(serverName, serverProfilePicture=b''):
        query = """
            INSERT INTO ClassServer (serverName, serverProfilePicture)
            VALUES (%s, %s);
        """
        values = (serverName, serverProfilePicture)

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