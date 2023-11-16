class Channeldb:
    @staticmethod
    def post_channel(channel):
        query = """
            INSERT INTO Channel (channelName) VALUES (%s)
        """
        values = (channel.get_channel_name,)
        channelID = Database.query(query, values)
        return channelID

    @staticmethod
    def get_channel(channelID):
        query = """
            SELECT * FROM Channel WHERE channelId = %s
        """
        result = Database.query(query, (channelID,), fetchVal=True)
        if result:
            return Channel(channelName=result['channelName'], channelID=result['channelId'])
        return None

    @staticmethod
    def patch_channel_name(channelID, new_channel_name):
        query = """
            UPDATE Channel SET channelName = %s WHERE channelId = %s
        """
        values = (new_channel_name, channelID)
        Database.query(query, values)
