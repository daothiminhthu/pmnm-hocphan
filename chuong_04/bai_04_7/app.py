
from flask import Flask, render_template

app = Flask(__name__)

THONG_TIN = {
    "ho_ten": "Nguyễn Văn An",
    "email": "an@example.com"
}

du_an = [
    {
        "ten": "Website bán hàng",
        "mo_ta": "Xây dựng website bán hàng bằng Flask và HTML, CSS.",
        "cong_nghe": "Python, Flask, HTML, CSS"
    },
    {
        "ten": "Ứng dụng quản lý sinh viên",
        "mo_ta": "Quản lý thông tin sinh viên và kết quả học tập.",
        "cong_nghe": "Python, Jinja2"
    },
    {
        "ten": "Trang cá nhân",
        "mo_ta": "Giới thiệu bản thân và các sản phẩm đã thực hiện.",
        "cong_nghe": "HTML, CSS, Bootstrap"
    }
]


@app.context_processor
def inject_thong_tin():
    return THONG_TIN


@app.route("/")
def trang_chu():
    return render_template("index.html")


@app.route("/hoc-van")
def hoc_van():
    return render_template("hoc_van.html")


@app.route("/du-an")
def trang_du_an():
    return render_template("du_an.html", du_an=du_an)


@app.route("/lien-he")
def lien_he():
    return render_template("lien_he.html")


if __name__ == "__main__":
    app.run(debug=True)
