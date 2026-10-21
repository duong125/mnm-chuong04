from flask import Flask, render_template

app = Flask(__name__)

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


# Đưa biến shop vào MỌI template (navbar, chân trang, trang 404...)
@app.context_processor
def inject_shop():
    return {"shop": SHOP}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html", menu=MENU)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
