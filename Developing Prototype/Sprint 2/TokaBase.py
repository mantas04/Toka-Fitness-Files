import mariadb #module to connect python with SQL database
import sys

class TokaBase: 
    def __init__(self):

        try:
            self.connection = mariadb.connect(
                user="Remote",  
                password="1234", 
                host="192.168.56.101",
                port=3306,
                database="tokadb" 
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB platform: {e}")# error message if mariadb doesnt connect
            sys.exit(1)

        self.cursor = self.connection.cursor()
    def getRegisterInfo_Premium(self,AccountType,Fname,Lname,email,gender,password):

        #Information given by the user is stored in these veriables above ^
        
        self.cursor.execute(f"INSERT tblcustomerid(FirstName,LastName,Gender,Email,Password,AccountType) values ('{Fname}','{Lname}','{gender}','{email}','{password}','{AccountType}');") 
        # The line above is inserting the given data which user has placed into veriables into the database with data fields which are in the sql database
        self.connection.commit() # locks data base and proceeds to process 
        
        return "ok premium" # returns this page or in this case these words if successfuly saved information

    def getRegisterInfo_Free(self,AccountType,Fname,Lname,email,gender,password):
        
        self.cursor.execute(f"INSERT tblcustomerid(FirstName,LastName,Gender,Email,Password,AccountType) values ('{Fname}','{Lname}','{gender}','{email}','{password}','{AccountType}');")
        self.connection.commit()
        
        return "ok free" # same as above




    def verifyLogin(self,email,password):
        self.cursor.execute(f"SELECT CustomerIdfr,AccountType FROM tblcustomerid WHERE Email = '{email}' and Password = '{password}';")
        result = self.cursor.fetchone()
        return result

    def cookie(self,Cookie,CustomerIdfr):
        self.cursor.execute(f"INSERT tblcookie(cookie,CustomerIdfr) values ('{Cookie}','{CustomerIdfr}');")
        self.connection.commit()


    def getCustomerId(self,Cookie):
        self.cursor.execute(f"SELECT CustomerIdfr FROM tblcookie WHERE Cookie ='{Cookie}';")
        CustomerIdHolder = self.cursor.fetchone()
        return CustomerIdHolder


    def getName(self, CustomerIdfr):
        self.cursor.execute(f"Select FirstName from tblcustomerid where CustomerIdfr = {CustomerIdfr}")
        result = self.cursor.fetchone()
        return result
    
    def Select(self, column, table, condition = None):
        self.cursor.execute(f"Select {column} from {table} {condition}")
        result = self.cursor.fetchone()
        return result
