from flask import Flask
from handy_methods.nested import inner_nested, nested_str
from methods import import_method
from .handy_methods.inner import *

app = Flask(__name__)


@app.route('/hi')
def hello_world():
    return "HELLO, World!!"


@app.route('/another')
def another():
    return "another route!"


def json_list_lk():
    x=3
    y=100
    d = "string in there"
    z=3000
    def wow():
        a= 3
        b=4
        c=4
        return "nested wow"
    return {0: ['hi', 'bye', 'no', d]}


@app.route('/user')
def get_user():
  return {'id': 2}

import_method()

nested_str()

inner_nested()

