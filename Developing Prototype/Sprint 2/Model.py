from flask import render_template,make_response

from hashlib import md5
from TokaBase import *

TokaDB = TokaBase()


class Model:
    def __init__(self):
        pass

    def getRegisterPage(self):
        return render_template('HomePage.html')
                                #Veriables received from Controller and goten by registerInfo
                                #which are then sent to the TokaDB(TokaBase.py)
    def getRegisterInfo_Premium(self,AccountType,Fname,Lname,email,gender,password):
        if AccountType == "Premium":
            return TokaDB.getRegisterInfo_Premium(AccountType,Fname,Lname,email,gender,password)
        else:
            return render_template('HomePage.html')

    def getRegisterInfo_Free(self,AccountType,Fname,Lname,email,gender,password):
        if AccountType == "Free":
            return TokaDB.getRegisterInfo_Free(AccountType,Fname,Lname,email,gender,password)
        else:
            return render_template('HomePage.html')




    def verifyLogin(self,email,password):
        results = TokaDB.verifyLogin(email,password)

        if results != None:
            AccountType = results[1]
            CustomerIdfr = results[0]
            
            text = email.encode('utf-8')
            Cookie = md5(text).hexdigest()
            #call function on tbl to add cookie and pass customers id
            TokaDB.cookie(Cookie,CustomerIdfr)
            
            if AccountType =="Free":
                result = TokaDB.getName(CustomerIdfr)
                name = result[0]
                LoginResponse = make_response(render_template('FreeDashboard.html', name = name))
                LoginResponse.set_cookie('Session', Cookie)
                return LoginResponse

            elif AccountType =="Premium":
                result = TokaDB.getName(CustomerIdfr)
                name = result[0]
                LoginResponse = make_response(render_template('PremiumDashboard.html',name = name))
                LoginResponse.set_cookie('Session', Cookie)
                return LoginResponse

        return render_template('LoginPage.html')


    def getLoginPage(self):
        return render_template('LoginPage.html')

        #getting dashboards depending on user

    def getFreeDash(self, Cookie):
        result = TokaDB.Select("CustomerIdfr", "tblcookie", f"WHERE Cookie = '{Cookie}'")
        CustomerIdfr = result[0]
        result = TokaDB.Select("FirstName", "tblCustomerid", f"WHERE CustomerIdfr = {CustomerIdfr}")
        name = result[0]
        return render_template('FreeDashboard.html', name = name)

    def getPremiumDash(self, Cookie):
        result = TokaDB.Select("CustomerIdfr", "tblcookie", f"WHERE Cookie = '{Cookie}'")
        CustomerIdfr = result[0]
        result = TokaDB.Select("FirstName", "tblCustomerid", f"WHERE CustomerIdfr = {CustomerIdfr}")
        name = result[0]
        return render_template('PremiumDashboard.html', name = name)
