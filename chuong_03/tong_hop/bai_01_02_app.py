from flask import Flask, request, url_for

app = Flask(__name__)

app.json.ensure_ascii = False


STUDENTS = {
    "23T1020001": {
        "name": "Nguyễn Văn An",
        "lop": "K47A",
        "scores": {
            "PMPM": 8.5,
            "CSDL": 7.0,
            "MHT": 9.0
        }
    },

    "23T1020002": {
        "name": "Trần Thị Bình",
        "lop": "K47A",
        "scores": {
            "PMPM": 6.0,
            "CSDL": 5.5,
            "MHT": 7.0
        }
    },

    "23T1020003": {
        "name": "Lê Hoàng Cường",
        "lop": "K47B",
        "scores": {
            "PMPM": 9.5,
            "CSDL": 9.0
        }
    },

    "23T1020004": {
        "name": "Phạm Minh Dũng",
        "lop": "K47B",
        "scores": {
            "PMPM": 4.0,
            "CSDL": 3.5,
            "MHT": 5.0
        }
    },

    "23T1020005": {
        "name": "Hoàng Thu Hà",
        "lop": "K47A",
        "scores": {}
    },

    "23T1020006": {
        "name": "Võ Quốc Khánh",
        "lop": "K47C",
        "scores": {
            "PMPM": 7.5,
            "MHT": 8.0
        }
    }
}


STYLE = """
<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #f3f6fa;
    color: #1f2937;
}

.container {
    width: 92%;
    max-width: 1100px;
    margin: 40px auto;
}

/* HEADER */

.header {
    background: white;
    padding: 28px 32px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.06);
}

.header h1 {
    margin: 0 0 8px;
    font-size: 30px;
    color: #111827;
}

.header p {
    margin: 0;
    color: #6b7280;
    font-size: 15px;
}

/* MENU */

.menu {
    display: flex;
    gap: 10px;
    margin-top: 22px;
}

.btn {
    display: inline-block;
    padding: 10px 17px;
    border-radius: 8px;
    background: #2563eb;
    color: white;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
}

.btn:hover {
    background: #1d4ed8;
}

.btn-light {
    background: #e5e7eb;
    color: #374151;
}

.btn-light:hover {
    background: #d1d5db;
}

/* STATISTICS */

.cards {
    display: flex;
    gap: 20px;
    margin-bottom: 25px;
}

.card {
    flex: 1;
    background: white;
    padding: 24px;
    border-radius: 14px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.06);
}

.card-title {
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 8px;
}

.card-number {
    font-size: 32px;
    font-weight: bold;
    color: #2563eb;
}

/* CONTENT BOX */

.box {
    background: white;
    padding: 28px;
    border-radius: 16px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.06);
}

.box h2 {
    margin-top: 0;
    margin-bottom: 20px;
}

/* FILTER */

.filters {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 22px;
}

.filter {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 8px;
    background: #f3f4f6;
    color: #374151;
    text-decoration: none;
    border: 1px solid #e5e7eb;
    font-size: 14px;
}

.filter:hover {
    background: #e5e7eb;
}

/* TABLE */

.table-wrapper {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background: #2563eb;
    color: white;
    padding: 14px;
    text-align: left;
    font-size: 14px;
}

td {
    padding: 14px;
    border-bottom: 1px solid #e5e7eb;
    font-size: 14px;
}

tbody tr:hover {
    background: #f8fafc;
}

td a {
    color: #2563eb;
    text-decoration: none;
    font-weight: 600;
}

td a:hover {
    text-decoration: underline;
}

/* BADGE */

.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 20px;
    background: #eff6ff;
    color: #1d4ed8;
    font-size: 13px;
    font-weight: 600;
}

/* DETAIL */

.detail {
    display: grid;
    grid-template-columns: 150px 1fr;
    row-gap: 15px;
    margin-bottom: 25px;
}

.detail-label {
    color: #6b7280;
    font-weight: 600;
}

.detail-value {
    font-weight: 500;
}

/* SCORE TABLE */

.score-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.score-table th {
    background: #f3f4f6;
    color: #374151;
}

.score-table td {
    border-bottom: 1px solid #e5e7eb;
}

/* EMPTY */

.empty {
    text-align: center;
    padding: 35px;
    color: #6b7280;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 13px;
    margin-top: 25px;
}

/* MOBILE */

@media (max-width: 700px) {

    .container {
        width: 95%;
        margin: 20px auto;
    }

    .cards {
        flex-direction: column;
    }

    .header h1 {
        font-size: 24px;
    }

    .detail {
        grid-template-columns: 1fr;
        row-gap: 5px;
    }

}

</style>
"""


def diem_trung_binh(scores):

    if not scores:
        return None

    return sum(scores.values()) / len(scores)



def xep_loai(diem):

    if diem is None:
        return "—"

    if diem >= 8:
        return "Giỏi"

    elif diem >= 6.5:
        return "Khá"

    elif diem >= 5:
        return "Trung bình"

    else:
        return "Yếu"


# CÂU 1 - TRANG CHỦ /

@app.route("/")
def index():

    # Tổng số sinh viên
    total_students = len(STUDENTS)

    # Lấy danh sách lớp trực tiếp từ dữ liệu
    classes = {
        student["lop"]
        for student in STUDENTS.values()
    }

    return f"""
<!DOCTYPE html>

<html lang="vi">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Quản lý sinh viên</title>

    {STYLE}

</head>

<body>

<div class="container">

    <div class="header">

        <h1>Quản lý sinh viên</h1>

        <p>
            Hệ thống quản lý thông tin và kết quả học tập
        </p>

        <div class="menu">

            <a class="btn"
               href="{url_for('student_list')}">

                Danh sách sinh viên

            </a>

            <a class="btn btn-light"
               href="{url_for('api_students')}">

                API sinh viên

            </a>

        </div>

    </div>


    <div class="cards">

        <div class="card">

            <div class="card-title">
                Tổng số sinh viên
            </div>

            <div class="card-number">
                {total_students}
            </div>

        </div>


        <div class="card">

            <div class="card-title">
                Số lớp
            </div>

            <div class="card-number">
                {len(classes)}
            </div>

        </div>

    </div>


    <div class="footer">

        Flask - Chương 3

    </div>

</div>

</body>

</html>
"""


# CÂU 2 - DANH SÁCH /students

@app.route("/students")
def student_list():

    # Lấy tham số ?lop=
    lop = request.args.get("lop", "").strip().lower()


    classes = sorted({
        student["lop"]
        for student in STUDENTS.values()
    })

    students = []

    for mssv, student in STUDENTS.items():

        # Nếu có truyền lop
        if lop:

            # Không phân biệt hoa thường
            if student["lop"].lower() != lop:
                continue

        students.append((mssv, student))

    filter_links = ""

    for class_name in classes:

        filter_links += f"""
        <a class="filter"
           href="{url_for(
               'student_list',
               lop=class_name
           )}">

            {class_name}

        </a>
        """

    rows = ""

    for mssv, student in students:

        diem = diem_trung_binh(
            student["scores"]
        )

        if diem is None:

            diem_text = "—"

        else:

            diem_text = f"{diem:.2f}"


        rows += f"""
        <tr>

            <td>

                <a href="{url_for(
                    'student_detail',
                    mssv=mssv
                )}">

                    {mssv}

                </a>

            </td>


            <td>
                {student["name"]}
            </td>


            <td>

                <span class="badge">
                    {student["lop"]}
                </span>

            </td>


            <td>
                {diem_text}
            </td>


            <td>

                <span class="badge">
                    {xep_loai(diem)}
                </span>

            </td>

        </tr>
        """

    if not students:

        rows = """
        <tr>

            <td colspan="5"
                class="empty">

                Không có sinh viên phù hợp.

            </td>

        </tr>
        """


    return f"""
<!DOCTYPE html>

<html lang="vi">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Danh sách sinh viên</title>

    {STYLE}

</head>

<body>

<div class="container">


    <div class="header">

        <h1>Danh sách sinh viên</h1>

        <p>
            Thông tin và kết quả học tập
        </p>

        <div class="menu">

            <a class="btn btn-light"
               href="{url_for('index')}">

                ← Trang chủ

            </a>

            <a class="btn"
               href="{url_for('api_students')}">

                API

            </a>

        </div>

    </div>


    <div class="box">

        <h2>Danh sách sinh viên</h2>


        <div class="filters">

            <a class="filter"
               href="{url_for('student_list')}">

                Tất cả

            </a>

            {filter_links}

        </div>


        <div class="table-wrapper">

            <table>

                <thead>

                    <tr>

                        <th>MSSV</th>

                        <th>Họ tên</th>

                        <th>Lớp</th>

                        <th>Điểm TB</th>

                        <th>Xếp loại</th>

                    </tr>

                </thead>


                <tbody>

                    {rows}

                </tbody>

            </table>

        </div>

    </div>


    <div class="footer">

        Có {len(students)} sinh viên được hiển thị

    </div>

</div>

</body>

</html>
"""


@app.route("/students/<mssv>")
def student_detail(mssv):

    student = STUDENTS.get(mssv)


    # Không tìm thấy
    if student is None:

        return """
        <h1>Không tìm thấy sinh viên</h1>

        <a href="/students">
            Quay lại danh sách
        </a>
        """, 404


    diem = diem_trung_binh(
        student["scores"]
    )


    if diem is None:

        diem_text = "—"

    else:

        diem_text = f"{diem:.2f}"


    # Tạo bảng điểm
    score_rows = ""

    for subject, score in student["scores"].items():

        score_rows += f"""
        <tr>

            <td>{subject}</td>

            <td>{score}</td>

        </tr>
        """


    if not score_rows:

        score_rows = """
        <tr>

            <td colspan="2"
                class="empty">

                Chưa có điểm.

            </td>

        </tr>
        """


    return f"""
<!DOCTYPE html>

<html lang="vi">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>{student["name"]}</title>

    {STYLE}

</head>

<body>

<div class="container">


    <div class="header">

        <h1>👤 Chi tiết sinh viên</h1>

        <p>
            Thông tin sinh viên và kết quả học tập
        </p>

    </div>


    <div class="box">

        <div class="detail">

            <div class="detail-label">
                MSSV
            </div>

            <div class="detail-value">
                {mssv}
            </div>


            <div class="detail-label">
                Họ tên
            </div>

            <div class="detail-value">
                {student["name"]}
            </div>


            <div class="detail-label">
                Lớp
            </div>

            <div class="detail-value">
                {student["lop"]}
            </div>


            <div class="detail-label">
                Điểm TB
            </div>

            <div class="detail-value">
                {diem_text}
            </div>


            <div class="detail-label">
                Xếp loại
            </div>

            <div class="detail-value">
                {xep_loai(diem)}
            </div>

        </div>


        <h2>Điểm các học phần</h2>


        <table class="score-table">

            <thead>

                <tr>

                    <th>Môn học</th>

                    <th>Điểm</th>

                </tr>

            </thead>


            <tbody>

                {score_rows}

            </tbody>

        </table>


        <div class="menu">

            <a class="btn btn-light"
               href="{url_for('student_list')}">

                ← Quay lại danh sách

            </a>

        </div>

    </div>

</div>

</body>

</html>
"""



@app.route("/api/students")
def api_students():

    result = []


    for mssv, student in STUDENTS.items():

        diem = diem_trung_binh(
            student["scores"]
        )


        result.append({

            "mssv": mssv,

            "name": student["name"],

            "lop": student["lop"],

            "diem_tb": diem,

            "xep_loai": xep_loai(diem)

        })


    return result


if __name__ == "__main__":

    app.run(
        debug=True,
        port=8000
    )
