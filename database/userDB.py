from .database import Database
class User:
    

    @staticmethod
    def createAccount(username,email, password,image):
        # print(cls.instance)
        value = Database.query(
            """
            INSERT INTO user(username,useremail,userpassword,userProfilePicture)
            VALUES (%s,%s,%s,%s)
            """,
            (username,email,password,image)
            )
        return value
    @staticmethod
    def getAccount(email, userID = None):
        value = Database.query(
            """
            SELECT * FROM user where useremail = %s;
            """,
            (email,),
            fetchVal = True
        )
        return value
    @staticmethod
    def deteleteAccount(email, userID =None):
        value = Database.query(
            """
            DELETE FROM user where useremail = %s;
            """,
            (email,)
        )
    # @staticmethod
    # def changeAccount(email, username,password, userID = None ):
    #     if userID 
    