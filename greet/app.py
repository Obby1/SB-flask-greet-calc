from flask import Flask
from flask import request

app= Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"


# python3 -m unittest test.py