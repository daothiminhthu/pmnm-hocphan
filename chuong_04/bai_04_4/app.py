
from flask import Flask, render_template

app = Flask(__name__)

sinh_vien = [
    {"ho_ten": "Nguyen Van An", "diem": 8.5},
    {"ho_ten": "Tran Thi Binh", "diem": 6.5},
    {"ho_ten": "Le Van Cuong", "diem": 4.0},
    {"ho_ten": "Pham Thi Dung", "diem": 9.0},
    {"ho_ten": "Hoang Minh Duc", "diem": 3.5}
]

@app.route("/")
def trang_chu():
    return render_template(
        "loc_sinh_vien.html",
        sinh_vien=sinh_vien
    )

if __name__ == "__main__":
    app.run(debug=True)
