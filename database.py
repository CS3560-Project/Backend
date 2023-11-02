import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
class Database:
    __instance = None
    
    def __init__(self,user,password, database_name,host = "localhost"):
        if Database.__instance is not None:
            raise Exception("instance already created")
        else:
            try:
                
                Database.__instance = mysql.connector.connect(user = user,
                password = password,
                database = database_name,
                host = host)
                x = Database.query("USE cpppm;")
                
                
                
                
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