from flask import Flask, render_template, request

app = Flask(__name__)


def doc_so(du_lieu, ten, gioi_han_min=None, gioi_han_max=None):
    if not du_lieu.strip():
        return None, f"Vui lòng nhập {ten}."

    try:
        so = float(du_lieu.strip().replace(",", "."))
    except ValueError:
        return None, f"{ten.capitalize()} phải là một số."

    if gioi_han_min is not None and so < gioi_han_min:
        return None, f"Giá trị phải từ {gioi_han_min} đến {gioi_han_max}."

    if gioi_han_max is not None and so > gioi_han_max:
        return None, f"Giá trị phải từ {gioi_han_min} đến {gioi_han_max}."

    return so, ""


@app.context_processor
def them_thong_tin_chung():
    return {"ten_website": "CalcSpace"}


@app.route("/")
def trang_chu():
    return render_template("index.html", active="home")


@app.route("/may-tinh", methods=["GET", "POST"])
def may_tinh():
    a = request.form.get("a", "")
    b = request.form.get("b", "")
    op = request.form.get("op", "+")
    ket_qua = None
    loi_a = loi_b = loi_op = ""

    if request.method == "POST":
        so_a, loi_a = doc_so(a, "số thứ nhất")
        so_b, loi_b = doc_so(b, "số thứ hai")

        if op not in ["+", "-", "*", "/"]:
            loi_op = "Phép toán không hợp lệ."

        if not loi_a and not loi_b and not loi_op:
            if op == "/" and so_b == 0:
                loi_b = "Không thể chia cho 0."
            else:
                if op == "+":
                    ket_qua = so_a + so_b
                elif op == "-":
                    ket_qua = so_a - so_b
                elif op == "*":
                    ket_qua = so_a * so_b
                elif op == "/":
                    ket_qua = so_a / so_b

    return render_template(
        "may_tinh.html",
        active="may_tinh",
        a=a, b=b, op=op, ket_qua=ket_qua,
        loi_a=loi_a, loi_b=loi_b, loi_op=loi_op
    )


@app.route("/tinh-diem", methods=["GET", "POST"])
def tinh_diem():
    cc = request.form.get("cc", "")
    gk = request.form.get("gk", "")
    ck = request.form.get("ck", "")

    loi_cc = loi_gk = loi_ck = ""
    diem_hp = None
    xep_loai = ""

    if request.method == "POST":
        diem_cc, loi_cc = doc_so(cc, "điểm chuyên cần", 0, 10)
        diem_gk, loi_gk = doc_so(gk, "điểm giữa kỳ", 0, 10)
        diem_ck, loi_ck = doc_so(ck, "điểm cuối kỳ", 0, 10)

        if not cc.strip() and not gk.strip() and not ck.strip():
            loi_cc = loi_gk = loi_ck = "Vui lòng nhập điểm."

        if not loi_cc and not loi_gk and not loi_ck:
            diem_hp = round(diem_cc * 0.1 + diem_gk * 0.3 + diem_ck * 0.6, 1)

            if diem_ck < 1:
                xep_loai = "F"
            elif diem_hp >= 8.5:
                xep_loai = "A"
            elif diem_hp >= 7:
                xep_loai = "B"
            elif diem_hp >= 5.5:
                xep_loai = "C"
            elif diem_hp >= 4:
                xep_loai = "D"
            else:
                xep_loai = "F"

    return render_template(
        "tinh_diem.html",
        active="tinh_diem",
        cc=cc, gk=gk, ck=ck,
        loi_cc=loi_cc, loi_gk=loi_gk, loi_ck=loi_ck,
        diem_hp=diem_hp, xep_loai=xep_loai
    )


@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    chieu_cao = request.form.get("chieu_cao", "")
    can_nang = request.form.get("can_nang", "")

    loi_chieu_cao = loi_can_nang = ""
    chi_so = None
    phan_loai = ""
    mau = ""
    can_nang_min = can_nang_max = None

    if request.method == "POST":
        cao, loi_chieu_cao = doc_so(chieu_cao, "chiều cao", 50, 250)
        nang, loi_can_nang = doc_so(can_nang, "cân nặng", 10, 300)

        if not chieu_cao.strip() and not can_nang.strip():
            loi_chieu_cao = loi_can_nang = "Vui lòng nhập dữ liệu."

        if not loi_chieu_cao and not loi_can_nang:
            cao_m = cao / 100
            chi_so = round(nang / (cao_m ** 2), 1)

            if chi_so < 18.5:
                phan_loai, mau = "Thiếu cân", "vang"
            elif chi_so < 23:
                phan_loai, mau = "Bình thường", "xanh"
            elif chi_so < 25:
                phan_loai, mau = "Thừa cân", "vang"
            else:
                phan_loai, mau = "Béo phì", "do"

            can_nang_min = round(18.5 * cao_m ** 2, 1)
            can_nang_max = round(22.9 * cao_m ** 2, 1)

    return render_template(
        "bmi.html",
        active="bmi",
        chieu_cao=chieu_cao, can_nang=can_nang,
        loi_chieu_cao=loi_chieu_cao, loi_can_nang=loi_can_nang,
        chi_so=chi_so, phan_loai=phan_loai, mau=mau,
        can_nang_min=can_nang_min, can_nang_max=can_nang_max
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)