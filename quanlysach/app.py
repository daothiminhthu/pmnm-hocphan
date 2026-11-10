import sqlite3
from flask import Flask, g, render_template, request, redirect, url_for, flash, abort

app = Flask(__name__)
app.secret_key = "quan-ly-sach"
DB = "books.db"
PALETTE = ["#a8402f", "#25666a", "#9c7418", "#3a4e9c", "#59752f", "#7c3f72", "#b05a28", "#41607f"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    price INTEGER NOT NULL DEFAULT 0,
    quantity INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(_):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    with sqlite3.connect(DB) as db:
        db.executescript(SCHEMA)


@app.template_global()
def cat_color(category_id):
    return PALETTE[(category_id - 1) % len(PALETTE)]


@app.template_filter("vnd")
def vnd(value):
    return f"{int(value or 0):,}".replace(",", ".") + " ₫"


def to_int(value, default=None):
    value = (value or "").strip()
    if not value:
        return default
    try:
        n = int(value)
    except ValueError:
        raise ValueError
    if n < 0:
        raise ValueError
    return n


@app.route("/")
def dashboard():
    db = get_db()
    stats = db.execute(
        """SELECT
            (SELECT COUNT(*) FROM categories) AS categories,
            COUNT(*) AS books,
            COALESCE(SUM(quantity), 0) AS stock,
            COALESCE(SUM(price * quantity), 0) AS value
        FROM books"""
    ).fetchone()
    by_category = db.execute(
        """SELECT c.id, c.name, COUNT(b.id) AS books, COALESCE(SUM(b.quantity), 0) AS stock
        FROM categories c LEFT JOIN books b ON b.category_id = c.id
        GROUP BY c.id ORDER BY books DESC, c.name"""
    ).fetchall()
    recent = db.execute(
        """SELECT b.*, c.name AS category FROM books b
        JOIN categories c ON c.id = b.category_id
        ORDER BY b.id DESC LIMIT 6"""
    ).fetchall()
    shelf = db.execute(
        "SELECT id, category_id, title FROM books ORDER BY category_id, id LIMIT 30"
    ).fetchall()
    low = db.execute(
        "SELECT id, category_id, title, quantity FROM books WHERE quantity <= 5 ORDER BY quantity, title LIMIT 5"
    ).fetchall()
    top = max((r["books"] for r in by_category), default=0)
    return render_template(
        "dashboard.html", stats=stats, by_category=by_category, recent=recent, shelf=shelf, low=low, top=top
    )


@app.route("/categories")
def categories():
    rows = get_db().execute(
        """SELECT c.*, COUNT(b.id) AS books FROM categories c
        LEFT JOIN books b ON b.category_id = c.id
        GROUP BY c.id ORDER BY c.name"""
    ).fetchall()
    return render_template("categories.html", categories=rows)


def get_category(category_id):
    row = get_db().execute("SELECT * FROM categories WHERE id = ?", (category_id,)).fetchone()
    if row is None:
        abort(404)
    return row


def save_category(category_id=None):
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    form = {"name": name, "description": description}
    if not name:
        flash("Vui lòng nhập tên danh mục.", "error")
        return form
    db = get_db()
    try:
        if category_id is None:
            db.execute("INSERT INTO categories (name, description) VALUES (?, ?)", (name, description))
        else:
            db.execute("UPDATE categories SET name = ?, description = ? WHERE id = ?", (name, description, category_id))
        db.commit()
    except sqlite3.IntegrityError:
        flash("Tên danh mục đã tồn tại.", "error")
        return form
    return None


@app.route("/categories/new", methods=["GET", "POST"])
def category_new():
    form = {}
    if request.method == "POST":
        form = save_category()
        if form is None:
            flash("Đã thêm danh mục.")
            return redirect(url_for("categories"))
    return render_template("category_form.html", category=None, form=form)


@app.route("/categories/<int:category_id>/edit", methods=["GET", "POST"])
def category_edit(category_id):
    category = get_category(category_id)
    form = dict(category)
    if request.method == "POST":
        form = save_category(category_id)
        if form is None:
            flash("Đã cập nhật danh mục.")
            return redirect(url_for("categories"))
    return render_template("category_form.html", category=category, form=form)


@app.post("/categories/<int:category_id>/delete")
def category_delete(category_id):
    get_category(category_id)
    db = get_db()
    db.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    db.commit()
    flash("Đã xoá danh mục và các sách thuộc danh mục.")
    return redirect(url_for("categories"))


@app.route("/books")
def books():
    db = get_db()
    category_id = request.args.get("category_id", type=int)
    q = request.args.get("q", "").strip()
    sql = """SELECT b.*, c.name AS category FROM books b
        JOIN categories c ON c.id = b.category_id WHERE 1 = 1"""
    params = []
    if category_id:
        sql += " AND b.category_id = ?"
        params.append(category_id)
    if q:
        sql += " AND (b.title LIKE ? OR b.author LIKE ?)"
        params += [f"%{q}%", f"%{q}%"]
    rows = db.execute(sql + " ORDER BY b.id DESC", params).fetchall()
    cats = db.execute("SELECT id, name FROM categories ORDER BY name").fetchall()
    return render_template("books.html", books=rows, categories=cats, category_id=category_id, q=q)


def get_book(book_id):
    row = get_db().execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if row is None:
        abort(404)
    return row


def save_book(book_id=None):
    form = {k: request.form.get(k, "").strip() for k in ("title", "author", "category_id", "year", "price", "quantity")}
    if not form["title"] or not form["author"]:
        flash("Vui lòng nhập tên sách và tác giả.", "error")
        return form
    try:
        category_id = to_int(form["category_id"])
        year = to_int(form["year"])
        price = to_int(form["price"], 0)
        quantity = to_int(form["quantity"], 0)
    except ValueError:
        flash("Năm, giá và số lượng phải là số nguyên không âm.", "error")
        return form
    db = get_db()
    if category_id is None or db.execute("SELECT 1 FROM categories WHERE id = ?", (category_id,)).fetchone() is None:
        flash("Vui lòng chọn danh mục.", "error")
        return form
    values = (category_id, form["title"], form["author"], year, price, quantity)
    if book_id is None:
        db.execute(
            "INSERT INTO books (category_id, title, author, year, price, quantity) VALUES (?, ?, ?, ?, ?, ?)", values
        )
    else:
        db.execute(
            "UPDATE books SET category_id = ?, title = ?, author = ?, year = ?, price = ?, quantity = ? WHERE id = ?",
            values + (book_id,),
        )
    db.commit()
    return None


def category_options():
    return get_db().execute("SELECT id, name FROM categories ORDER BY name").fetchall()


@app.route("/books/new", methods=["GET", "POST"])
def book_new():
    form = {"category_id": request.args.get("category_id", "")}
    if request.method == "POST":
        form = save_book()
        if form is None:
            flash("Đã thêm sách.")
            return redirect(url_for("books"))
    return render_template("book_form.html", book=None, form=form, categories=category_options())


@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
def book_edit(book_id):
    book = get_book(book_id)
    form = {k: ("" if v is None else v) for k, v in dict(book).items()}
    if request.method == "POST":
        form = save_book(book_id)
        if form is None:
            flash("Đã cập nhật sách.")
            return redirect(url_for("books"))
    return render_template("book_form.html", book=book, form=form, categories=category_options())


@app.post("/books/<int:book_id>/delete")
def book_delete(book_id):
    get_book(book_id)
    db = get_db()
    db.execute("DELETE FROM books WHERE id = ?", (book_id,))
    db.commit()
    flash("Đã xoá sách.")
    return redirect(request.referrer or url_for("books"))


init_db()

if __name__ == "__main__":
    app.run(debug=True)
