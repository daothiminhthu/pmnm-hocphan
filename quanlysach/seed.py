import sqlite3
from app import DB, init_db

init_db()
db = sqlite3.connect(DB)
if db.execute("SELECT COUNT(*) FROM categories").fetchone()[0] == 0:
    cats = [
        ("Văn học", "Tiểu thuyết, truyện ngắn, thơ"),
        ("Công nghệ thông tin", "Lập trình, cơ sở dữ liệu, mạng máy tính"),
        ("Kinh tế", "Quản trị, marketing, tài chính"),
        ("Thiếu nhi", "Truyện tranh và sách giáo dục cho trẻ em"),
    ]
    db.executemany("INSERT INTO categories (name, description) VALUES (?, ?)", cats)
    books = [
        (1, "Dế Mèn phiêu lưu ký", "Tô Hoài", 1941, 45000, 30),
        (1, "Số đỏ", "Vũ Trọng Phụng", 1936, 68000, 12),
        (1, "Tắt đèn", "Ngô Tất Tố", 1939, 52000, 4),
        (2, "Clean Code", "Robert C. Martin", 2008, 320000, 8),
        (2, "Java Core", "Cay S. Horstmann", 2019, 280000, 15),
        (2, "Giáo trình Cơ sở dữ liệu", "Nguyễn Văn Ba", 2018, 95000, 25),
        (3, "Nghĩ giàu và làm giàu", "Napoleon Hill", 1937, 89000, 18),
        (4, "Doraemon tập 1", "Fujiko F. Fujio", 1970, 22000, 60),
    ]
    db.executemany(
        "INSERT INTO books (category_id, title, author, year, price, quantity) VALUES (?, ?, ?, ?, ?, ?)", books
    )
    db.commit()
db.close()
