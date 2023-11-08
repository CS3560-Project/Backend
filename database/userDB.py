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
        pass
    