# 🧩 AI 8-Puzzle Game
Giới thiệu

AI-8Puzzle-Game là một dự án mô phỏng trò chơi 8-Puzzle được xây dựng bằng Python và Pygame. Dự án cho phép người chơi tự giải câu đố hoặc sử dụng các thuật toán tìm kiếm của Trí tuệ nhân tạo (Artificial Intelligence) để tìm lời giải tối ưu.

Mục tiêu của dự án là giúp người học hiểu cách hoạt động của các thuật toán tìm kiếm thông qua việc trực quan hóa quá trình giải bài toán.

---

## 📌 Tính năng

- Giao diện đồ họa được xây dựng bằng Pygame.
- Chơi trò chơi 8-Puzzle bằng chuột.
- Trộn bàn cờ ngẫu nhiên.
- Kiểm tra trạng thái thắng.
- Hiển thị số bước đã thực hiện.
- Hiển thị thời gian giải.
- Hỗ trợ giải tự động bằng các thuật toán AI.
- Hoạt ảnh mô phỏng từng bước giải.
- Thiết kế giao diện hiện đại với màu sắc dễ nhìn.

---

## 🛠️ Công nghệ

- Python 3.12+
- Pygame Community Edition (pygame-ce)
- Heapq
- Collections
- Time
- ath

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