from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)

# Danh sách 95 mục
danh_sach = [
    {"id": i, "ten": f"Mục số {i}"}
    for i in range(1, 96)
]


# Trang chủ tự chuyển sang trang danh sách
@app.route("/")
def trang_chu():
    return redirect(url_for("items", page=1))


# Danh sách có phân trang
@app.route("/items")
def items():
    page_text = request.args.get("page", "1")

    # Kiểm tra page có phải số nguyên không
    try:
        page = int(page_text)
    except (ValueError, TypeError):
        abort(404)

    so_muc_moi_trang = 10
    total_items = len(danh_sach)
    total_pages = (total_items + so_muc_moi_trang - 1) // so_muc_moi_trang

    # Trang không hợp lệ trả về 404
    if page < 1 or page > total_pages:
        abort(404)

    start = (page - 1) * so_muc_moi_trang
    end = start + so_muc_moi_trang
    danh_sach_trang = danh_sach[start:end]

    return render_template(
        "items.html",
        danh_sach=danh_sach_trang,
        page=page,
        total_pages=total_pages,
        total_items=total_items
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)