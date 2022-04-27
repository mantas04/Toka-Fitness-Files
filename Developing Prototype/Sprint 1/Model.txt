from http.client import ImproperConnectionState
from flask import render_template,make_response

from hashlib import md5
from TokaBase import *

TokaDB = TokaBase()


class Model:
    def __init__(self):
        pass

    def getHomepage(self):
        return render_template('HomePage.html')

    def getLoginpage(self):
        return render_template('LoginPage.html')
