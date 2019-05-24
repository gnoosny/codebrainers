from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'witaj'

@app.route('/hello')
def hello_world():
    return "hello world"

@app.route('/auto')
def auto():
    return "<img src=http://bi.gazeta.pl/im/8d/af/16/z23787149IH,Skoda-Fabia-2018.jpg>"