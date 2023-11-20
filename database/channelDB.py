from .database import Database


class ChannelThe:

    @staticmethod

    def post_channel(channelName):
  
        value = Database.query( 

            """
            INSERT INTO channel(channelName) VALUES (%s)
            """,

            (channelName,),
            getID = True
            )
        print("THIS IS GETTING CALLED")
        return value


    @staticmethod
    def get_channel(channelID):
        print("call")

        value = Database.query(
         """
            SELECT * FROM Channel WHERE channelId = %s
        """,
        (channelID,),
        isDictionary = True,
        fetchVal = True
        )
        print(type(value[0]))
        print(value)
        return value[0]

    

    @staticmethod
    def patch_channel_name(channelID, new_channel_name):
        query = """
            UPDATE Channel SET channelName = %s WHERE channelId = %s
        """
        values = (new_channel_name, channelID)
        Database.query(query, values)