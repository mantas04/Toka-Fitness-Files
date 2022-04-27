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
                LoginResponse = make_response(redirect('/FreePage')) # redirect user to Free page
                LoginResponse.set_cookie('Session', Cookie) #giving user the cookies for the browser
                return LoginResponse #returns all login response

            elif AccountType =="Premium":
                LoginResponse = make_response(redirect('/PremiumPage'))
                LoginResponse.set_cookie('Session', Cookie)
                return LoginResponse

        return render_template('LoginFailPage.html') # if login fails returns fail page template 


    def getFreeDash(self, Cookie):
        result = TokaDB.Select("CustomerIdfr", "tblCookie", f"WHERE Cookie = '{Cookie}'") # looks for customeridfr in tblcookie where cookie is same as cookie
        CustomerIdfr = result[0]
        result = TokaDB.Select("FirstName", "tblCustomerid", f"WHERE CustomerIdfr = {CustomerIdfr}") # looks for first name in tblcustomerid where customer id is same ascustomerid variable
        name = result[0]
        return render_template('FreeDashboard.html', name = name)

    def getPremiumDash(self, Cookie):
        result = TokaDB.Select("CustomerIdfr", "tblCookie", f"WHERE Cookie = '{Cookie}'")
        CustomerIdfr = result[0]
        result = TokaDB.Select("FirstName", "tblCustomerid", f"WHERE CustomerIdfr = {CustomerIdfr}")
        name = result[0]
        return render_template('PremiumDashboard.html', name = name)




    def getLoginPage(self):
        return render_template('LoginPage.html') #render template returns pages

    def getBlogsPage(self):
        return render_template('Blogs.html') 


    def getPushupsPage(self):
        return render_template('PushUps.html')

    def pushUpsDone(self,cookie, increment):
        result = TokaDB.Select("CustomerIdfr","tblcookie", f"WHERE Cookie ='{cookie}'")
        IdObtained = result[0]
        return TokaDB.pushUpsDone(increment,IdObtained) # sends these veriables to tokadb(TokaBase)

    def getSquatsPage(self):
        return render_template('Squats.html')

    def SquatssDone(self,cookie, increment):
        result = TokaDB.Select("CustomerIdfr","tblcookie", f"WHERE Cookie ='{cookie}'")
        IdObtained = result[0]
        return TokaDB.SquatssDone(increment,IdObtained)

    def getRecord(self):
        results = TokaDB.getWorkouts() # results are the items retrived from database
        records = []
        for result in results:
            records.append(result)
        return render_template("Records.html", records = records) #shows records in a line being the results which user has saved

    