from flask import render_template,make_response,redirect

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
            TokaDB.getRegisterInfo_Premium(AccountType,Fname,Lname,email,gender,password)
            return redirect('/login')
        else:
            return render_template('RegisterPage.html')

    def getRegisterInfo_Free(self,AccountType,Fname,Lname,email,gender,password):
        if AccountType == "Free":
            TokaDB.getRegisterInfo_Free(AccountType,Fname,Lname,email,gender,password)
            return redirect('/login')
        else:
            return render_template('RegisterPage.html')





    def verifyLogin(self,email,password):
        results = TokaDB.verifyLogin(email,password)

        

        if results != None:
            AccountType = results[1]
            CustomerIdfr = results[0]
            
            text = email.encode('utf-8')
            Cookie = md5(text).hexdigest()
            #call function on tdb to add cookie and pass customers id
            TokaDB.cookie(Cookie,CustomerIdfr)
            
            if AccountType =="Free":
                LoginResponse = make_response(redirect('/FreePage'))
                LoginResponse.set_cookie('Session', Cookie)
                return LoginResponse

            elif AccountType =="Premium":
                LoginResponse = make_response(redirect('/PremiumPage'))
                LoginResponse.set_cookie('Session', Cookie)
                return LoginResponse

        return render_template('LoginFailPage.html')


    def getFreeDash(self, Cookie):
        result = TokaDB.Select("CustomerIdfr", "tblCookie", f"WHERE Cookie = '{Cookie}'")
        CustomerIdfr = result[0]
        result = TokaDB.Select("FirstName", "tblCustomerid", f"WHERE CustomerIdfr = {CustomerIdfr}")
        name = result[0]
        return render_template('FreeDashboard.html', name = name)

    def getPremiumDash(self, Cookie):
        result = TokaDB.Select("CustomerIdfr", "tblCookie", f"WHERE Cookie = '{Cookie}'")
        CustomerIdfr = result[0]
        result = TokaDB.Select("FirstName", "tblCustomerid", f"WHERE CustomerIdfr = {CustomerIdfr}")
        name = result[0]
        return render_template('PremiumDashboard.html', name = name)




    def getLoginPage(self):
            return render_template('LoginPage.html')