from datetime import timedelta

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    session,
    flash,
    request
)

from forms import RegisterForm


from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config["SECRET_KEY"] = "bai_tap_chuong_5_secret_key"
app.config["WTF_CSRF_ENABLED"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)

csrf = CSRFProtect(app)


# Tài khoản mẫu từ Bài 4
USERS = {
    "an": {
        "password": "an123456",
        "email": "an@gmail.com"
    },
    "on": {
        "password": "on123456",
        "email": "on@gmail.com"
    }
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data.strip()
        email = form.email.data.strip()

        # Kiểm tra tên đăng nhập đã tồn tại
        if username in USERS:
            flash(
                "Tên đăng nhập đã được sử dụng.",
                "danger"
            )
            return render_template(
                "register.html",
                form=form
            )

        # Kiểm tra email đã tồn tại
        for user in USERS.values():
            if user["email"].lower() == email.lower():
                flash(
                    "Email đã được sử dụng.",
                    "danger"
                )
                return render_template(
                    "register.html",
                    form=form
                )

        # Kiểm tra đồng ý điều khoản
        if not form.agree.data:
            flash(
                "Bạn phải đồng ý với điều khoản.",
                "warning"
            )
            return render_template(
                "register.html",
                form=form
            )

        # Thêm tài khoản mới
        USERS[username] = {
            "password": form.password.data,
            "email": email
        }

        flash("Đăng ký thành công!", "success")

        return redirect(url_for("login"))

    return render_template(
        "register.html",
        form=form
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if (
            username in USERS
            and USERS[username]["password"] == password
        ):
            session["user"] = username

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
    if "user" not in session:
        flash(
            "Vui lòng đăng nhập để xem hồ sơ.",
            "warning"
        )
        return redirect(url_for("login"))

    username = session["user"]
    user = USERS.get(username)

    if user is None:
        session.pop("user", None)
        flash("Tài khoản không tồn tại.", "danger")
        return redirect(url_for("login"))

    return render_template(
        "profile.html",
        username=username,
        email=user["email"]
    )


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)

    flash("Bạn đã đăng xuất.", "info")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)