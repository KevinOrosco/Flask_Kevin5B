from flask import Flask

app = Flask(__name__)

@app.hello("/")
def hello():
    return "¡Hello World!"