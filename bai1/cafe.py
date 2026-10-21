from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

SHOP = {"name": "Cà phê Sông Hương",
        "address": "12 Lê Lợi, Huế",
        "open": 7, "close": 22}

PROMOTIONS = [
    "Giảm 10% cho sinh viên",
    "Mua 2 tặng 1 vào thứ Hai",
]


@app.route("/")
def index():
    # ?gio=23 để thử; không truyền thì lấy giờ thật của máy
    gio = request.args.get("gio", type=int)
    if gio is None:
        gio = datetime.now().hour

    # giờ mở cửa tính là mở, giờ đóng cửa tính là đóng
    dang_mo = SHOP["open"] <= gio < SHOP["close"]
    trang_thai = "đang mở cửa" if dang_mo else "đã đóng cửa"

    return render_template("index.html",
                           shop=SHOP,
                           gio=gio,
                           dang_mo=dang_mo,
                           trang_thai=trang_thai,
                           promotions=PROMOTIONS)


if __name__ == "__main__":
    app.run(debug=True)
