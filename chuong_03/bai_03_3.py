from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name="bạn"):
    return f"Xin chào, {escape(name)}!"