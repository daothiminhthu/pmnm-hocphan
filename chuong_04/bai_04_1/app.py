from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def trang_chu():
    return render_template(
        "profile.html",
        ho_ten="Nguyễn Văn An",
        nam_sinh=2005,
        nganh="Công nghệ phần mềm",
        ky_nang=["Python", "HTML", "CSS", "Flask"]
    )

if __name__ == "__main__":
    app.run(debug=True)