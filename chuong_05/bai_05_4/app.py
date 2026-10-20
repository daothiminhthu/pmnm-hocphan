from flask import Flask, render_template, request

app = Flask(__name__)


def kiem_tra_so(gia_tri, ten, gioi_han_min, gioi_han_max):
    if not gia_tri.strip():
        return None, f"Vui lòng nhập {ten}."

    try:
        so = float(gia_tri.replace(",", "."))
    except ValueError:
        return None, f"{ten.capitalize()} phải là một số."

    if so < gioi_han_min or so > gioi_han_max:
        return None, f"Giá trị phải từ {gioi_han_min} đến {gioi_han_max}."

    return so, ""


@app.route("/", methods=["GET", "POST"])
def tinh_bmi():
    chieu_cao = ""
    can_nang = ""

    loi_chieu_cao = ""
    loi_can_nang = ""

    bmi = None
    phan_loai = ""
    mau = ""

    can_nang_min = None
    can_nang_max = None

    if request.method == "POST":
        chieu_cao = request.form.get("chieu_cao", "").strip()
        can_nang = request.form.get("can_nang", "").strip()

        if not chieu_cao and not can_nang:
            loi_chieu_cao = "Vui lòng nhập chiều cao."
            loi_can_nang = "Vui lòng nhập cân nặng."
        else:
            cao, loi_chieu_cao = kiem_tra_so(
                chieu_cao, "chiều cao", 50, 250
            )

            nang, loi_can_nang = kiem_tra_so(
                can_nang, "cân nặng", 10, 300
            )

            if not loi_chieu_cao and not loi_can_nang:
                chieu_cao_m = cao / 100

                bmi = round(nang / (chieu_cao_m ** 2), 1)

                # Phân loại theo tiêu chuẩn người châu Á trên slide
                if bmi < 18.5:
                    phan_loai = "Thiếu cân"
                    mau = "vang"
                elif bmi < 23:
                    phan_loai = "Bình thường"
                    mau = "xanh"
                elif bmi < 25:
                    phan_loai = "Thừa cân"
                    mau = "vang"
                else:
                    phan_loai = "Béo phì"
                    mau = "do"

                # Cân nặng tương ứng với BMI từ 18.5 đến 22.9
                can_nang_min = round(18.5 * chieu_cao_m ** 2, 1)
                can_nang_max = round(22.9 * chieu_cao_m ** 2, 1)

    return render_template(
        "index.html",
        chieu_cao=chieu_cao,
        can_nang=can_nang,
        loi_chieu_cao=loi_chieu_cao,
        loi_can_nang=loi_can_nang,
        bmi=bmi,
        phan_loai=phan_loai,
        mau=mau,
        can_nang_min=can_nang_min,
        can_nang_max=can_nang_max
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)