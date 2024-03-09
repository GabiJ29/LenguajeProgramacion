import mysql.connector
import os

class MySQLBD:
    def __init__(self, host, user, password, database):
        self.host= host
        self.user= user
        self.password= password
        self.database= database
        self.connection = None

    def connect(self):
        try:
            if(self.connect == None):
                self.connection= mysql.connector.connect(
                    host= self.host,
                    user= self.user,
                    password= self.password,
                    database= self.database
                )
                print("Conectado")

        except mysql.connector.ERROR as error:
            print("Error mientras se estaban conectando {}".format(error))



database = MySQLBD("localhost", "Root", "", "testlp")

database.disconect

database.connect()