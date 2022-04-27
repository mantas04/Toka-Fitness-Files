from flask import Flask, request #importing flask 
from Model import *

app = Flask(__name__) 
model = Model()


@app.route("/") # '/' will be used to route to pages using flask functionality
def Homepage():
    return model.getHomepage()

@app.route("/login")
def Loginpage():
    return model.getLoginpage()



if __name__ == '__main__': app.run(host='0.0.0.0') #used for local host