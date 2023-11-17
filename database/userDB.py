from .database import Database
class User:
    

    @staticmethod
    def createAccount(username,email, password,imageID):
        # print(cls.instance)
        value = Database.query(
            """
            INSERT INTO user(username,email,password,profilePictureID)
            VALUES (%s,%s,%s,%s)
            """,
            (username,email,password,imageID),
            getID = True
            )
        return value
    @staticmethod
    def getAccount(email, userID = None):
        value = Database.query(
            """
            SELECT * FROM user where email = %s;
            """,
            (email,),
            isDictionary = True,
            fetchVal = True
        )
        return value
    @staticmethod
    def deteleteAccount(email, userID =None):
        value = Database.query(
            """
            DELETE FROM user where email = %s;
            """,
            (email,)
        )
    @staticmethod
    def changeAccount(email, username,password, userID = None ):
        Database.query(
            """
            UPDATE user
            SET
                
                password =%s,
                username = %s
            WHERE 
                email = %s
            """,
            (username,password,email)
        )
    