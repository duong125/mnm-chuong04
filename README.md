# Chương 4 · Template với Jinja2 (Flask)

Quán "Cà phê Sông Hương" – 4 bài thực hành, mỗi bài là một thư mục độc lập.

| Bài | Nội dung | Chạy | Địa chỉ |
|-----|----------|------|---------|
| 1 | Trang chủ quán, trạng thái mở/đóng, khuyến mãi | `python bai1/cafe.py` | http://127.0.0.1:5000/?gio=9 |
| 2 | Bảng thực đơn, filter `vnd`, thống kê | `python bai2/cafe.py` | http://127.0.0.1:5000/menu |
| 3 | Website 3 trang, `base.html`, `super()`, 404 | `python bai3/cafe.py` | http://127.0.0.1:5000/ |
| 4 | include, macro, phân trang `/menu?page=N` | `python bai4/cafe.py` | http://127.0.0.1:5000/menu |

## Cài đặt

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```
