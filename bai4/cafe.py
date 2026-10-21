import math

from flask import Flask, abort, render_template, request

app = Flask(__name__)

PER_PAGE = 3

SHOP = {"name": "Cà phê Sông Hương",
        "address": "12 Lê Lợi, Huế",
        "phone": "0234 3888 999"}

MENU = [
    {"id": 1, "name": "Cà phê đen", "price": 20000, "image": "ca-phe-den.jpg"},
    {"id": 2, "name": "Cà phê sữa", "price": 25000, "image": "ca-phe-sua.jpg"},
    {"id": 3, "name": "Bạc xỉu", "price": 30000, "image": "bac-xiu.jpg"},
    {"id": 4, "name": "Trà đào", "price": 40000, "image": "tra-dao.jpg"},
    {"id": 5, "name": "Trà sữa", "price": 35000, "image": "tra-sua.jpg"},
    {"id": 6, "name": "Nước cam", "price": 30000, "image": "nuoc-cam.jpg"},
    {"id": 7, "name": "Sinh tố bơ", "price": 35000, "image": "sinh-to-bo.jpg"},
]


@app.template_filter("vnd")
def vnd(value):
    return f"{value:,.0f} đ".replace(",", ".")


@app.context_processor
def inject_shop():
    return {"shop": SHOP}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/menu")
def menu():
    # ?page=abc -> type=int thất bại -> dùng mặc định 1 (như trang 1)
    page = request.args.get("page", 1, type=int)
    pages = max(1, math.ceil(len(MENU) / PER_PAGE))

    # page=0, page=-1, page=4 ... -> không tồn tại -> 404
    if page < 1 or page > pages:
        abort(404)

    start = (page - 1) * PER_PAGE
    items = MENU[start:start + PER_PAGE]

    return render_template("menu.html",
                           items=items, page=page, pages=pages,
                           total=len(MENU))


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
