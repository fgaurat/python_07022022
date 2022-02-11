from flask import Flask

app = Flask(__name__)




@app.route('/hello')
def hello():
    return "<h1>Hello</h1>"

@app.route('/hello1')
def hello1():
    return "<h1>Hello1</h1>"

@app.route('/hello2')
def hello2():
    return "<h1>Hello2</h1>"