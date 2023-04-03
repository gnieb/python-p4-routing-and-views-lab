#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print("hello, world")
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f"{param}"

@app.route('/count/<int:int>') 
def count(int):
   return f'''
   
   '''

@app.route('/math/<num1><operation><num2>')
def math(num1, operation, num2):
    pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)
