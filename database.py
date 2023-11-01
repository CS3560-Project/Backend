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
                
                
                
            except Error as e:
                print(e)
    @staticmethod
    def getInstance(user, password,database_name,host = "localhost"):
        if Database.__instance is None:
            Database(user = user,password = password, database_name= database_name,host=host)
        return Database.__instance
    @staticmethod
    def close_instance():
        Database.__instance.close()

    @classmethod
    def query(cls):
        cls.__instance
        

