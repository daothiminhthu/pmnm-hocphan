from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)

# Danh sách menu: endpoint và nhãn hiển thị
MENU = [
    {"endpoint": "index", "label": "Trang chủ"},
    {"endpoint": "about", "label": "Giới thiệu"},
    {"endpoint": "contact", "label": "Liên hệ"}
]


@app.context_processor
def inject_globals():
    # Hàm xác định mục menu đang được mở
    def is_active(endpoint):
        return "active" if request.endpoint == endpoint else ""

    # Các biến này có thể dùng trong mọi template
    return {
        "menu": MENU,
        "site_name": "MiniBlog",
        "current_year": date.today().year,
        "is_active": is_active
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)