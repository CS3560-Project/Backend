import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
class Database:
    __instance = None
    
    def __init__(self,user,password, database_name,host = "localhost"):
        '''
            Singleton class the init method should never be called
            any instances of this class should be called through the getInstance() method

        '''

        if Database.__instance is not None:
            raise Exception("instance already created")
        else:
            try:
                
                Database.__instance = mysql.connector.connect(user = user,
                password = password,
                database = database_name,
                host = host)
                Database.query("USE cpppm;")
                Database.query("""
                    CREATE TABLE IF NOT EXISTS ClassServer(
                        serverID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        serverName varchar(255) NOT NULL,
                        serverProfilePicture BLOB NOT NULL
                    );"""
                )
                Database.query("""
                    CREATE TABLE IF NOT EXISTS Image(
                        imageID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        image BLOB NOT NULL,
                        size varchar(20) NOT NULL,
                        type varchar(10) NOT NULL
                    );
                """)
                Database.query("""
            CREATE TABLE IF NOT EXISTS User(
                userID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                userName VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
                    );
                """)


                
                
                
                
            except Error as e:
                print(e)
    @staticmethod
    def getInstance(user= None, password= None,database_name= None,host = "localhost"):
        if Database.__instance is None:
            Database(user = user,password = password, database_name= database_name,host=host)
        return Database.__instance
    @staticmethod
    def close_instance():
        Database.__instance.close()
    
    @classmethod
    def query(cls,query, data = None, isMulti = False):
        cursor = cls.__instance.cursor()
        value = cursor.execute(query,params = None, multi = isMulti)

        cursor.close()
        Database.__instance.commit()
        return value

        

database = Database.getInstance(
    user = os.environ.get("MYSQL_DB_USER"),
    password= os.environ.get("MYSQL_DB_PASS"),
    database_name=  os.environ.get("MYSQL_DB_NAME")
)
