from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Blog!"
app.config.from_object("config")