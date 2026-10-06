from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Trang chủ"


@app.route("/about")
def about():
    return "Giới thiệu"


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    return f"Bài viết {post_id}"


@app.route("/user/<username>")
def user_profile(username):
    return f"Trang cá nhân {username}"


@app.route("/search")
def search():
    return "Tìm kiếm"


if __name__ == "__main__":
    app.run(debug=True, port=8000)