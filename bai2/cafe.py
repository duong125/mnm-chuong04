from flask import Flask, render_template

app = Flask(__name__)

MENU = [
    {"name": "cà phê đen", "price": 20000, "available": True},
    {"name": "bạc xỉu", "price": 30000, "available": False},
    {"name": "cà phê sữa", "price": 25000, "available": True},
    {"name": "trà đào", "price": 40000, "available": True},
    {"name": "nước cam", "price": 35000, "available": True},
]


# Filter tự viết: 25000 -> "25.000 đ"
@app.template_filter("vnd")
def vnd(value):
    return f"{value:,.0f} đ".replace(",", ".")


@app.route("/menu")
def menu():
    return render_template("menu.html", menu=MENU)


if __name__ == "__main__":
    app.run(debug=True)
