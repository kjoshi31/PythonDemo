from flask import Flask
from handy_methods.nested import inner_nested, nested_str
from methods import import_method
from .handy_methods.inner import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "HELLO, World!!"


@app.route('/another')
def another():
    return "another route!"


def json_list():
    x=3
    y=100
    z=3000
    a = x + y + z
    return {0: ['hi', 'bye', 'no']}


@app.route('/user')
def get_user():
    return {'id': 1}

import_method()

nested_str()

inner_nested()

print('hello world')

print('wow')

print('wow')