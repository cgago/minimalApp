from flask import Flask

app = Flask(__name__)

@app.rote('/')
def index{}:
    return "Hola mundo"
