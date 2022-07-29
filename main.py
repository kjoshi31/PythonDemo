from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "HELLO, World!!"


@app.route('/another')
def another():
    return "another route!"


def json_list():
    return {0: ['hi', 'bye', 'no']}


def say_hello():
    return "hi"

@app.route('/user')
def get_user():
    return {'id': 1}
