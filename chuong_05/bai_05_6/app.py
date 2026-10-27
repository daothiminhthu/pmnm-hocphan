from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

# Khóa bí mật dùng cho session
app.secret_key = "bai_tap_dang_nhap_123456"

# Tài khoản mẫu
USERS = {
    "an": "an123456",
    "on": "on123456"
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Nếu đã đăng nhập thì chuyển về trang chủ
    if "user" in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        remember = request.form.get("remember")

        # Kiểm tra tài khoản và mật khẩu
        if username in USERS and USERS[username] == password:
            session["user"] = username

            # Ghi nhớ đăng nhập nếu được chọn
            session.permanent = bool(remember)

            flash(
                f"Đăng nhập thành công. Xin chào {username}!",
                "success"
            )

            return redirect(url_for("index"))

        flash(
            "Sai tên đăng nhập hoặc mật khẩu.",
            "danger"
        )

    return render_template("login.html")


@app.route("/profile")
def profile():
    # Chưa đăng nhập thì quay về trang đăng nhập
    if "user" not in session:
        flash("Vui lòng đăng nhập để xem hồ sơ.", "warning")
        return redirect(url_for("login"))

    return render_template("profile.html")


@app.route("/logout", methods=["POST"])
def logout():
    # Xóa thông tin đăng nhập
    session.pop("user", None)
    session.permanent = False

    flash("Bạn đã đăng xuất.", "info")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)