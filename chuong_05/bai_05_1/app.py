from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def may_tinh():
    a = ""
    b = ""
    op = "+"
    ket_qua = None
    loi_a = ""
    loi_b = ""
    loi_op = ""

    if request.method == "POST":
        a = request.form.get("a", "").strip()
        b = request.form.get("b", "").strip()
        op = request.form.get("op", "+")

        so_a = None
        so_b = None

        # Kiểm tra số thứ nhất
        if not a:
            loi_a = "Vui lòng nhập số thứ nhất."
        else:
            try:
                so_a = float(a.replace(",", "."))
            except ValueError:
                loi_a = "Số thứ nhất không hợp lệ."

        # Kiểm tra số thứ hai
        if not b:
            loi_b = "Vui lòng nhập số thứ hai."
        else:
            try:
                so_b = float(b.replace(",", "."))
            except ValueError:
                loi_b = "Số thứ hai không hợp lệ."

        # Kiểm tra phép toán
        if op not in ["+", "-", "*", "/"]:
            loi_op = "Phép toán không hợp lệ."

        # Thực hiện tính toán khi dữ liệu hợp lệ
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
        "index.html",
        a=a,
        b=b,
        op=op,
        ket_qua=ket_qua,
        loi_a=loi_a,
        loi_b=loi_b,
        loi_op=loi_op
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)