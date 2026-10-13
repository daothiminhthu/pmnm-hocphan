
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

san_pham = [
    {
        "ten": "Laptop Dell",
        "gia": 15000000,
        "ngay_nhap": datetime(2026, 9, 15)
    },
    {
        "ten": "Chuột không dây",
        "gia": 250000,
        "ngay_nhap": datetime(2026, 10, 1)
    },
    {
        "ten": "Bàn phím cơ",
        "gia": 850000,
        "ngay_nhap": None
    },
    {
        "ten": "Tai nghe",
        "gia": 1200000,
        "ngay_nhap": datetime(2026, 10, 5)
    }
]


@app.template_filter("vnd")
def dinh_dang_vnd(value):
    return f"{value:,.0f}".replace(",", ".") + " ₫"


@app.template_filter("ngay")
def dinh_dang_ngay(value, fmt="%d/%m/%Y"):
    if value is None:
        return ""

    if isinstance(value, str):
        value = datetime.fromisoformat(value)

    return value.strftime(fmt)


@app.route("/")
def danh_sach():
    tong_gia_tri = sum(sp["gia"] for sp in san_pham)

    return render_template(
        "danh_sach_san_pham.html",
        san_pham=san_pham,
        tong_gia_tri=tong_gia_tri
    )


if __name__ == "__main__":
    app.run(debug=True)
