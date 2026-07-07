# 🧩 AI 8-Puzzle Game

Đây là dự án xây dựng trò chơi **8-Puzzle** bằng Python kết hợp với Pygame.

> 🚧 Dự án đang được phát triển.

---

## 📌 Mục tiêu

- Xây dựng trò chơi 8-Puzzle.
- Áp dụng thuật toán BFS.
- Áp dụng thuật toán A*.
- So sánh hiệu năng giữa các thuật toán.

---

## 🛠️ Công nghệ

- Python
- Pygame CE
- Pillow
- Git & GitHub

---

## 📂 Tiến độ

- [x] Khởi tạo dự án
- [x] Giao diện
- [x] Logic bàn cờ
- [x] BFS
- [x] A*
- [x] Image Puzzle

---
## 🛠️ Cài đặt và chạy dự án

Yêu cầu hệ thống
- **Python**: Phiên bản 3.10 trở lên (Hỗ trợ tốt nhất 3.12, 3.13 và cả bản preview 3.14).
- **Thư viện**: 
  - `pygame-ce`: Phiên bản cộng đồng của Pygame, hỗ trợ tốt các đời Python mới.
  - `Pillow`: Xử lý cắt ghép ảnh.

---

Dự án sử dụng Python cơ bản và thư viện Pygame, có thể chạy thẳng trên mọi hệ điều hành (Windows/macOS/Linux).

**Bước 1:** Đảm bảo máy tính đã cài đặt **Python 3.10** hoặc mới hơn.

**Bước 2:** Di chuyển vào thư mục dự án và thiết lập môi trường:

```bash
# Tạo môi trường ảo (Khuyên dùng để tránh xung đột)
python -m venv .venv

# Kích hoạt môi trường ảo:
# - Windows: .venv\Scripts\activate
# - macOS/Linux: source .venv/bin/activate

# Cập nhật pip và cài đặt thư viện
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**Bước 3:** Khởi chạy trò chơi:

```bash
python main.py
```

> **Lưu ý**: Dự án sử dụng `pygame-ce` để đảm bảo hoạt động ổn định trên các phiên bản Python mới nhất (3.12+). Nếu bạn đã cài đặt `pygame` bản cũ, hãy gỡ ra trước khi cài đặt requirements.