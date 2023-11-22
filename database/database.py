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
                    CREATE TABLE IF NOT EXISTS Image(
                        imageID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        image MEDIUMTEXT NOT NULL,
                        imageType VARCHAR(10) NOT NULL
                        
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS ClassServer(
                        serverID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        serverName varchar(255) NOT NULL
                        
                    );""")
                Database.query("""
                    CREATE TABLE IF NOT EXISTS User(
                        userID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        userName varchar(255) NOT NULL,
                        email varchar(255) UNIQUE NOT NULL,
                        password varchar(255) NOT NULL,
                        profilePictureID int NOT NULL,
                        FOREIGN KEY (profilePictureID) references Image(imageID) ON DELETE CASCADE
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS UserServers(
                        userID INT NOT NULL,
                        serverID INT NOT NULL,
                        PRIMARY KEY (userID, serverID),
                        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
                        FOREIGN KEY (serverID) REFERENCES ClassServer(serverID) ON DELETE CASCADE
                    );
                """)
                Database.query("""
                    CREATE TABLE IF NOT EXISTS Channel(
                        channelId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        channelName varchar(255) NOT NULL,
                        serverID INT NOT NULL,
                        FOREIGN KEY (serverID) REFERENCES ClassServer(serverID) ON DELETE CASCADE
                    );
                """)

                Database.query("""
                    CREATE TABLE IF NOT EXISTS Message(
                        messageID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                        

                        message varchar(255) NOT NULL,
                        
                        userID INT NOT NULL,
                        timeSent DATETIME  NOT NULL,
                        edited BOOLEAN DEFAULT false,
                        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE
                        
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
                    CREATE TABLE IF NOT EXISTS CourseSection(
                        sectionId INT NOT NULL,
                        courseName varchar(255) NOT NULL,
                        serverID INT NOT NULL,
                        PRIMARY KEY (courseName, sectionId),
                        
                        FOREIGN KEY (serverID) REFERENCES classServer(serverID) ON DELETE CASCADE
                    );
                """)
                Database.query(
                    """
                    CREATE TABLE IF NOT EXISTS ServerMessage(
                        ChannelID INT NOT NULL,
                        ServerID INT NOT NULL,
                        MessageID INT NOT NULL,
                        PRIMARY KEY (ChannelID,ServerID,MessageID),
                        FOREIGN KEY (messageID) REFERENCES Message(messageID) ON DELETE CASCADE,
                        FOREIGN KEY (serverID) REFERENCES ClassServer(serverID) ON DELETE CASCADE,
                        FOREIGN KEY (channelID) REFERENCES Channel(channelID) ON DELETE CASCADE

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
    def query(cls, querys, data=None, isMulti=False, fetchVal=False, getID=False, isDictionary=False):
        """
            Use fetchVal if you want to geet the result
            use getID to get the previous value id of the insert
        """
        with cls.__instance.cursor(dictionary=isDictionary, buffered=True)as cursor:

            cursor.execute(querys, params=data, multi=isMulti)
            value = None
            if fetchVal:

                value = cursor.fetchall()
            if getID:
                value = cursor.lastrowid

        Database.__instance.commit()
        return value


database = Database.getInstance(
    user=os.environ.get("MYSQL_DB_USER"),
    password=os.environ.get("MYSQL_DB_PASS"),
    database_name=os.environ.get("MYSQL_DB_NAME")
)
