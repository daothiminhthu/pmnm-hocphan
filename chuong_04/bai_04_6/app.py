
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def trang_chu():
    content = "<script>alert('Xin chào')</script>"
    html_content = "<strong>Thông báo an toàn</strong>"

    return render_template(
        "xss.html",
        content=content,
        html_content=html_content
    )


if __name__ == "__main__":
    app.run(debug=True)
