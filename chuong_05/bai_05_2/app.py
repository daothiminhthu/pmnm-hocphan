from flask import Flask, render_template, request

app = Flask(__name__)


def kiem_tra_diem(du_lieu, ten_o):
    """Kiểm tra điểm nhập vào và trả về điểm hoặc thông báo lỗi."""

    if not du_lieu.strip():
        return None, f"Vui lòng nhập điểm {ten_o}."

    try:
        diem = float(du_lieu.replace(",", "."))
    except ValueError:
        return None, f"Điểm {ten_o} phải là một số."

    if diem < 0 or diem > 10:
        return None, f"Điểm {ten_o} phải từ 0 đến 10."

    return diem, ""


@app.route("/", methods=["GET", "POST"])
def tinh_diem():
    cc = ""
    gk = ""
    ck = ""

    loi_cc = ""
    loi_gk = ""
    loi_ck = ""

    diem_hp = None
    xep_loai = ""

    if request.method == "POST":
        cc = request.form.get("cc", "")
        gk = request.form.get("gk", "")
        ck = request.form.get("ck", "")

        # Trường hợp cả 3 ô đều trống
        if not cc.strip() and not gk.strip() and not ck.strip():
            loi_cc = "Vui lòng nhập điểm."
            loi_gk = "Vui lòng nhập điểm."
            loi_ck = "Vui lòng nhập điểm."
        else:
            diem_cc, loi_cc = kiem_tra_diem(cc, "chuyên cần")
            diem_gk, loi_gk = kiem_tra_diem(gk, "giữa kỳ")
            diem_ck, loi_ck = kiem_tra_diem(ck, "cuối kỳ")

            # Chỉ tính khi cả 3 điểm hợp lệ
            if not loi_cc and not loi_gk and not loi_ck:
                diem_hp = round(
                    diem_cc * 0.1
                    + diem_gk * 0.3
                    + diem_ck * 0.6,
                    1
                )

                # Điểm cuối kỳ dưới 1 là điểm liệt
                if diem_ck < 1:
                    xep_loai = "F"
                elif diem_hp >= 8.5:
                    xep_loai = "A"
                elif diem_hp >= 7.0:
                    xep_loai = "B"
                elif diem_hp >= 5.5:
                    xep_loai = "C"
                elif diem_hp >= 4.0:
                    xep_loai = "D"
                else:
                    xep_loai = "F"

    return render_template(
        "index.html",
        cc=cc,
        gk=gk,
        ck=ck,
        loi_cc=loi_cc,
        loi_gk=loi_gk,
        loi_ck=loi_ck,
        diem_hp=diem_hp,
        xep_loai=xep_loai
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)