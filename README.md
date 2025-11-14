# Ứng Dụng An Sao Tử Vi

Phần mềm tính toán và phân tích lá số tử vi theo phương pháp truyền thống Việt Nam.

## Mô tả

Đây là ứng dụng console-based được viết hoàn toàn bằng Python, cho phép người dùng tính toán lá số tử vi một cách chính xác theo phương pháp truyền thống Việt Nam. Ứng dụng hỗ trợ:

- Tính toán Can Chi (Thiên Can, Địa Chi) của năm, tháng, ngày, giờ
- Chuyển đổi giữa Âm lịch và Dương lịch
- Xác định 12 cung trong lá số tử vi
- An 14 sao chính diệu và các sao phụ diệu
- Tính Tứ Hóa (Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ)
- Phân tích Ngũ hành và sinh khắc
- Xuất kết quả lá số dưới dạng text

## Cấu trúc dự án

```
an_sao_tu_vi/
├── src/
│   ├── core/              # Các module cốt lõi
│   │   ├── can_chi.py     # Thiên Can, Địa Chi
│   │   ├── am_lich.py     # Chuyển đổi Âm Dương lịch
│   │   ├── cung_menh.py   # 12 cung tử vi
│   │   └── ngu_hanh.py    # Ngũ hành, sinh khắc
│   ├── stars/             # Hệ thống sao
│   │   ├── chinh_dieu.py  # 14 sao chính diệu
│   │   ├── phu_dieu.py    # Các sao phụ diệu
│   │   └── an_sao.py      # Thuật toán an sao
│   ├── analysis/          # Phân tích lá số
│   │   └── la_so.py       # Class chính LaSo
│   └── ui/                # Giao diện người dùng
│       └── console.py     # Console interface
├── main.py                # Entry point
├── requirements.txt       # Dependencies (không có)
└── README.md             # File này
```

## Yêu cầu hệ thống

- Python 3.7 trở lên
- Hệ điều hành: Linux, macOS, Windows
- Không cần cài đặt thư viện bên ngoài (chỉ dùng Python standard library)

## Cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd an_sao_tu_vi
```

2. Không cần cài đặt dependencies (ứng dụng không sử dụng thư viện bên ngoài)

## Sử dụng

### Chạy ứng dụng console:

```bash
python3 main.py
```

hoặc

```bash
python main.py
```

### Các chức năng chính:

1. **Tạo lá số tử vi mới**: Nhập thông tin ngày giờ sinh (Âm hoặc Dương lịch)
2. **Hiển thị lá số**: Xem toàn bộ lá số với 12 cung và các sao
3. **Phân tích cung Mệnh**: Xem chi tiết cung Mệnh và đánh giá
4. **Xem thông tin các cung**: Xem từng cung cụ thể (Phụ Mẫu, Quan Lộc, v.v.)
5. **Chuyển đổi Âm Dương lịch**: Công cụ chuyển đổi lịch
6. **Lưu lá số**: Xuất lá số ra file text

## Ví dụ

### Tính lá số cho ngày 15/05/1990, 14h:

```python
from src.analysis.la_so import LaSo

# Tạo lá số
la_so = LaSo(
    ngay_dl=15,
    thang_dl=5,
    nam_dl=1990,
    gio=14,
    gioi_tinh="Nam"
)

# Hiển thị lá số đầy đủ
print(la_so.hien_thi_la_so_day_du())

# Phân tích cung Mệnh
phan_tich = la_so.phan_tich_cung_menh()
print(phan_tich)

# Lưu ra file
la_so.luu_la_so_txt("la_so.txt")
```

## Tính năng chi tiết

### 1. Can Chi System
- 10 Thiên Can: Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý
- 12 Địa Chi: Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi
- Tính Can Chi cho năm, tháng, ngày, giờ

### 2. Chuyển đổi Âm Dương lịch
- Sử dụng thuật toán chính xác dựa trên Jean Meeus
- Hỗ trợ tháng nhuận

### 3. 12 Cung Tử Vi
- Mệnh, Phụ Mẫu, Phúc Đức, Điền Trạch, Quan Lộc, Nô Bộc
- Thiên Di, Tật Ách, Tài Bạch, Tử Tức, Phu Thê, Huynh Đệ

### 4. Hệ thống Sao
- **14 Sao chính diệu**: Tử Vi, Thiên Cơ, Thái Dương, Vũ Khúc, Thiên Đồng, Liêm Trinh, Thiên Phủ, Thái Âm, Tham Lang, Cự Môn, Thiên Tướng, Thiên Lương, Thất Sát, Phá Quân
- **Sao phụ diệu**: Văn Xương, Văn Khúc, Tả Phụ, Hữu Bật, Thiên Khôi, Thiên Việt, Lộc Tồn, Thiên Mã, v.v.
- **Tứ Hóa**: Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ

### 5. Ngũ Hành
- Kim, Mộc, Thủy, Hỏa, Thổ
- Phân tích tương sinh, tương khắc
- Đánh giá cân bằng ngũ hành

## Lưu ý

- Ứng dụng tính toán theo phương pháp truyền thống Việt Nam
- Kết quả mang tính chất tham khảo
- Thuật toán an sao được đơn giản hóa cho mục đích học tập và nghiên cứu

## Phát triển tiếp

Các tính năng có thể mở rộng:
- [ ] Thêm nhiều sao phụ diệu hơn
- [ ] Phân tích đại vận, tiểu vận
- [ ] Xuất lá số dưới dạng PDF/HTML
- [ ] Thêm hệ thống giải nghĩa chi tiết
- [ ] GUI với Tkinter hoặc web interface

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng:
1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## Giấy phép

Dự án này được phát hành dưới giấy phép MIT.

## Tác giả

Phát triển bởi Claude & Contributors

## Liên hệ

Nếu có bất kỳ câu hỏi hoặc đề xuất nào, vui lòng tạo issue trên GitHub.
