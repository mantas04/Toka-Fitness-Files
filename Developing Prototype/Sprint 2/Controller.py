from flask import Flask, request #importing flask 
from Model import *

app = Flask(__name__) 
model = Model()


@app.route("/") # '/' will be used to route to pages using flask functionality

@app.route("/register", methods = ["POST"])
def getRegisterInfo():
    Form = request.form #requesting form from html 
    AccountType = Form.get("AccountType") #is a hidden field in form will tell people which account type is which
    Fname = Form.get("Fname")
    Lname = Form.get("Lname")
    gender = Form.get("gender")
    email = Form.get("email")
    password = Form.get("Password")
    

    #This will see which account user has registered with once submit button is clicked in the forms
    #this uses the accountType veriable
    if AccountType == "Premium": 
        return model.getRegisterInfo_Premium(AccountType,Fname,Lname,email,gender,password) # These veriables are sent to model
    elif AccountType =="Free": 
        return model.getRegisterInfo_Free(AccountType,Fname,Lname,email,gender,password)
    else: 
     
        return model.getRegisterPage() # if nothing is submited it returns user back to register page



@app.route("/login", methods = ["POST" ,"GET"])
def getLoginPage():
    
    if request.method == "POST":
        Form = request.form
        
        email = Form.get("email")
        password = Form.get("password")
        
        return model.verifyLogin(email, password)
    
    return model.getLoginPage()

@app.route("/FreePage")
def getFreeDashboard():
    if request.cookies.get("Session"):
        Cookie = request.cookies.get("Session")
        return model.getFreeDash(Cookie)
    return model.getLoginPage()

@app.route("/PremiumPage")
def getPremiumDashboard():
    if request.cookies.get("Session"):
        Cookie = request.cookies.get("Session")
        return model.getPremiumDash(Cookie)
    return model.getLoginPage()



if __name__ == '__main__': app.run(host='0.0.0.0') #used for local host