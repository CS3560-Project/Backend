from .database import Database
class User:
    instance = Database.getInstance()
    
    @classmethod
    def createAccount(cls,username,email, password):
        cls.instance.query(
            """
            INSERT INTO account(username,email,password)
            VALUES (%s,)
            """
            )