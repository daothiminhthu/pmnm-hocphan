
from flask import Flask, render_template

app = Flask(__name__)


# Filter định dạng tiền Việt Nam
@app.template_filter("vnd")
def dinh_dang_vnd(gia):
    return f"{gia:,.0f}".replace(",", ".") + " ₫"


# Danh sách 8 sản phẩm
san_pham = [
    {"ten": "Tai nghe Bluetooth", "gia": 350000, "con_hang": True},
    {"ten": "Chuột không dây", "gia": 180000, "con_hang": True},
    {"ten": "Bàn phím cơ", "gia": 650000, "con_hang": False},
    {"ten": "Giá đỡ laptop", "gia": 220000, "con_hang": True},
    {"ten": "Loa mini", "gia": 420000, "con_hang": True},
    {"ten": "Đèn bàn LED", "gia": 150000, "con_hang": False},
    {"ten": "Sạc điện thoại", "gia": 120000, "con_hang": True},
    {"ten": "USB 64GB", "gia": 190000, "con_hang": True}
]


@app.route("/")
def trang_chu():
    return render_template("san_pham.html", san_pham=san_pham)


if __name__ == "__main__":
    app.run(debug=True, port=5000)