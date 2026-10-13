from flask import Flask, render_template

app = Flask(__name__)

THONG_TIN = {
    "ho_ten": "Nguyễn Văn An",
    "email": "an@example.com"
}

du_an = [
    {
        "ten": "Website bán hàng",
        "mo_ta": "Xây dựng website bán hàng bằng Flask.",
        "cong_nghe": "Python, Flask"
    },
    {
        "ten": "Quản lý sinh viên",
        "mo_ta": "Quản lý thông tin và điểm sinh viên.",
        "cong_nghe": "Python, Jinja2"
    },
    {
        "ten": "Website cá nhân",
        "mo_ta": "Giới thiệu bản thân và các dự án đã làm.",
        "cong_nghe": "HTML, CSS"
    }
]

@app.context_processor
def inject_thong_tin():
    return THONG_TIN

@app.route("/")
def trang_chu():
    return render_template("index.html", du_an=du_an)

@app.route("/hoc-van")
def hoc_van():
    return render_template("hoc_van.html")

@app.route("/du-an")
def trang_du_an():
    return render_template("index.html", du_an=du_an)

@app.route("/lien-he")
def lien_he():
    return render_template("lien_he.html")

if __name__ == "__main__":
    app.run(debug=True)