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