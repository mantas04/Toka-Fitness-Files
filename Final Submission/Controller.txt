from flask import Flask, request #importing flask 
from Model import *

app = Flask(__name__) 
model = Model()


@app.route("/") # '/' will be used to route to pages using flask functionalit       #Looks for route in search bar being something like localhost:5000/
def RegisterPage(): #function named register page as i will be calling register page
    return model.getRegisterPage()   #returns item from model (being the template)

@app.route("/register", methods = ["POST"])
def getRegisterInfo():
    Form = request.form #requesting form from html 
    AccountType = Form.get("AccountType") #is a hidden field in form will tell people which account type is which
    Fname = Form.get("Fname")
    Lname = Form.get("Lname")
    gender = Form.get("gender")
    email = Form.get("email")
    password = Form.get("password")
    

    #This will see which account user has registered with once submit button is clicked in the forms
    #this uses the accountType veriable
    if AccountType == "Premium": 
        return model.getRegisterInfo_Premium(AccountType,Fname,Lname,email,gender,password) # These veriables are sent to model
    elif AccountType =="Free": 
        return model.getRegisterInfo_Free(AccountType,Fname,Lname,email,gender,password)
    else: 
     
        return model.getRegisterPage() # if nothing is submited it returns user back to register page



@app.route("/login", methods = ["POST" ,"GET"]) # gets the users request to go to login
def getLoginPage():
    
    if request.method == "POST": # if request is equal to post
        Form = request.form # form equal request form from login page
        
        email = Form.get("Email") #get email from the login
        password = Form.get("Password") # get password from the login
        
        return model.verifyLogin(email, password) # return veriables to model
    
    return model.getLoginPage() #if its not a post then go to login page in model


@app.route("/FreePage")# gets the users request to go to FreePage
def getFreeDashboard():
    if request.cookies.get("Session"): #requesting cookies to get session from browser
        Cookie = request.cookies.get("Session") # if request is gained then 
        return model.getFreeDash(Cookie)# return cookie to model with getfreedash
    return model.getLoginPage()

@app.route("/PremiumPage")# gets the users request to go to PremiumPage
def getPremiumDashboard():
    if request.cookies.get("Session"):
        Cookie = request.cookies.get("Session")
        return model.getPremiumDash(Cookie)
    return model.getLoginPage()

@app.route("/pushups", methods = ["POST" ,"GET"])
def getPushupsPage():
    return model.getPushupsPage()

@app.route("/blogs", methods = ["POST","GET"])
def getBlogsPage():
    return model.getBlogsPage()

@app.route("/savepushups", methods = ["POST" ,"GET"])
def pushUpsDone():
    args = request.args
    cookie = request.cookies.get('Session')
    return model.pushUpsDone(cookie, args["increment"]) #args from pushupws page being ?increment

@app.route("/squats", methods = ["POST" ,"GET"])
def getSquatsPage():
    return model.getSquatsPage()


@app.route("/savesquats", methods = ["POST" ,"GET"])
def SquatssDone():
    args = request.args
    cookie = request.cookies.get('Session')
    return model.SquatssDone(cookie, args["increment"]) #args from squats page being ?increment


    
@app.route("/records")
def record():  
    return model.getRecord()

if __name__ == '__main__': app.run(host='0.0.0.0') #used for local host