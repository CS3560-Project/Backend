from .database import Database

class ChannelThe:

    @staticmethod
    def post_channel(channelName, serverID):
        value = Database.query( 
            """
            INSERT INTO Channel(channelName, serverID) VALUES (%s, %s)
            """,
            (channelName, serverID),
            getID=True
        )
        print("THIS IS GETTING CALLED")
        return value

    @staticmethod
    def get_channel(channelID):

        value = Database.query(
            """
            SELECT * FROM Channel WHERE channelId = %s
            """,
            (channelID,),
            isDictionary=True,
            fetchVal=True
        )
        print(value)
        return value[0]
    
    
    @staticmethod
    def get_channel_from_server(serverID):
        value = Database.query(
            """
            SELECT * FROM Channel WHERE serverID = %s
            """,
            (serverID,),
            isDictionary=True,
            fetchVal=True
        )
        print(value)
        print(value[0])
        print("\n\n\n\n")
        return value
    


    @staticmethod
    def patch_channel_name(channelID, new_channel_name):
        query = """
            UPDATE Channel SET channelName = %s WHERE channelId = %s
        """
        values = (new_channel_name, channelID)
        Database.query(query, values)

    def delete_channel(channelID):
            query = """
                DELETE FROM Channel WHERE channelId = %s
            """
            values = (channelID,)
            Database.query(query, values)
