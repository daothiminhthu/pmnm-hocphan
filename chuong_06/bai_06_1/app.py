
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# 1. Khoi tao Flask
app = Flask(__name__)

# 2. Cau hinh ket noi co so du lieu SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sinhvien.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True)

with app.app_context():
    os.makedirs(app.instance_path, exist_ok=True)
    db.create_all()
    print("Da tao co so du lieu va bang Student!")

@app.route('/')
def index():
    return "Ket noi co so du lieu thanh cong!"


@app.route('/add_student')
def add_student():
    danh_sach = [
        Student(name='Nguyen Van A', age=20, email='vana@gmail.com'),
        Student(name='Tran Thi B', age=21, email='thib@gmail.com'),
        Student(name='Le Van C', age=22, email='vanc@gmail.com'),
        Student(name='Pham Thi D', age=20, email='thid@gmail.com'),
        Student(name='Hoang Van E', age=23, email='vane@gmail.com')
    ]

    db.session.add_all(danh_sach)
    db.session.commit()

    return "Them 5 sinh vien thanh cong!"


# 7. Hien thi danh sach sinh vien bang Template
@app.route('/students')
def get_students():
    danh_sach = Student.query.all()

    return render_template(
        'students.html',
        danh_sach=danh_sach
    )


if __name__ == '__main__':
    app.run(debug=True)
