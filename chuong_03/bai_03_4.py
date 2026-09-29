from flask import Flask

app = Flask(__name__)


@app.route("/square/<int:n>")
def square(n):
    return f"Bình phương của {n} là {n * n}"