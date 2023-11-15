import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()


class Database:
    __instance = None

    def __init__(self, user, password, database_name, host="localhost"):
        '''
            Singleton class the init method should never be called
            any instances of this class should be called through the getInstance() method

        '''

        if Database.__instance is not None:
            raise Exception("instance already created")
        else:
            try:

                Database.__instance = mysql.connector.connect(user=user,
                                                              password=password,

                                                              host=host)
                Database.query("CREATE DATABASE IF NOT EXISTS cpppm;")
                Database.query("USE cpppm;")
                Database.query("""
                    CREATE TABLE IF NOT EXISTS ClassServer(
                        serverID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        serverName varchar(255) NOT NULL,
                        serverProfilePicture BLOB NOT NULL
                    );""")
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
                        userName varchar(255) NOT NULL,
                        userEmail varchar(255) NOT NULL,
                        userPassword varchar(255) NOT NULL,
                        userProfilePicture BLOB NOT NULL
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS UserServers(
                        userServersUserID INT NOT NULL,
                        userServersServerID INT NOT NULL,
                        PRIMARY KEY (userServersUserID, userServersServerID),
                        FOREIGN KEY (userServersUserID) REFERENCES User(userID) ON DELETE CASCADE,
                        FOREIGN KEY (userServersServerID) REFERENCES ClassServer(serverID) ON DELETE CASCADE
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS Message(
                        messageID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        message varchar(255) NOT NULL,
                        sender INT NOT NULL,
                        timeSent TIMESTAMP NOT NULL,
                        edited BOOLEAN NOT NULL,
                        FOREIGN KEY (sender) REFERENCES User(userID) ON DELETE CASCADE
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS MessageImage(
                        messageID INT NOT NULL,
                        imageID INT NOT NULL,
                        PRIMARY KEY (messageID, imageID),
                        FOREIGN KEY (messageID) REFERENCES Message(messageID) ON DELETE CASCADE,
                        FOREIGN KEY (imageID) REFERENCES Image(imageID) ON DELETE CASCADE
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS Course(
                        courseId varchar(10) NOT NULL,
                        courseName varchar(255) NOT NULL,
                        PRIMARY KEY (courseId)
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS CourseSection(
                        sectionId INT NOT NULL,
                        courseId varchar(10) NOT NULL
                        classCapacity INT NOT NULL,
                        instructorName varchar(255) NOT NULL,
                        PRIMARY KEY (courseId, sectionId),
                        FOREIGN KEY (courseId) REFERENCES COURSE(courseId) ON DELETE CASCADE
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS Channel(
                        channelId INT NOT NULL,
                        channelName varchar(255) NOT NULL,
                        PRIMARY KEY (channelId)
                    );
                """)
            except Error as e:
                print(e)

    @staticmethod
    def getInstance(user=None, password=None, database_name=None, host="localhost"):
        if Database.__instance is None:
            Database(user=user, password=password,
                     database_name=database_name, host=host)
        return Database.__instance

    @staticmethod
    def close_instance():
        Database.__instance.close()

    @classmethod
    def query(cls, querys, data=None, isMulti=False):

        cursor = cls.__instance.cursor()
        value = cursor.execute(querys, params=data, multi=isMulti)

        cursor.close()
        Database.__instance.commit()
        return value


database = Database.getInstance(
    user=os.environ.get("MYSQL_DB_USER"),
    password=os.environ.get("MYSQL_DB_PASS"),
    database_name=os.environ.get("MYSQL_DB_NAME")
)
