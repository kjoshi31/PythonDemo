from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "HELLO, World!!"

@app.route('/another')
def another():
    return "another route!"