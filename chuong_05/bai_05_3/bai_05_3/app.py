from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def trang_chu():
    return render_template("index.html")


@app.route("/may-tinh")
def may_tinh():
    return """
    <h1>Máy tính cơ bản</h1>
    <p>Đây là liên kết đến Bài 1.</p>
    <a href="/">Quay về trang chủ</a>
    """


@app.route("/tinh-diem")
def tinh_diem():
    return """
    <h1>Tính điểm học phần</h1>
    <p>Đây là liên kết đến Bài 2.</p>
    <a href="/">Quay về trang chủ</a>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5000)