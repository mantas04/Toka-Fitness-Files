import mariadb #module to connect python with SQL database
import sys

class TokaBase: 
    def __init__(self):
        try:
            self.connection = mariadb.connect(
                user = "Remote", 
                password = "qwerty",
                host = "192.168.56.101",
                port = 3306,
                database = 'tokadb'
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB platform: {e}")# error message if mariadb doesnt connect
            sys.exit(1)

        self.cursor = self.connection.cursor()