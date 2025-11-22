# Hệ Thống Quản Lý Sân Bay - Airport Management System

Hệ thống quản lý sân bay và chuyến bay được xây dựng bằng Flask, cung cấp các chức năng quản lý chuyến bay, vé, hành khách, nhân viên và báo cáo doanh thu.

## 📋 Mục Lục

- [Tính Năng](#tính-năng)
- [Công Nghệ Sử Dụng](#công-nghệ-sử-dụng)
- [Cài Đặt](#cài-đặt)
- [Cấu Hình](#cấu-hình)
- [Chạy Ứng Dụng](#chạy-ứng-dụng)
- [Cấu Trúc Dự Án](#cấu-trúc-dự-án)
- [API Endpoints](#api-endpoints)
- [Tài Liệu API](#tài-liệu-api)
- [Docker](#docker)
- [Phát Triển](#phát-triển)

## ✨ Tính Năng

### Quản Lý Chuyến Bay
- Thêm, sửa, xóa chuyến bay
- Quản lý sân bay trung gian
- Quản lý hạng vé cho từng chuyến bay
- Tìm kiếm chuyến bay theo thời gian, sân bay đi/đến
- Kiểm tra số ghế còn trống/đã đặt

### Quản Lý Sân Bay
- Quản lý thông tin sân bay
- Kiểm tra trạng thái hoạt động của sân bay

### Quản Lý Vé
- Đặt vé chuyến bay
- Quản lý thông tin vé
- Tích hợp thanh toán VNPay

### Quản Lý Hành Khách
- Thêm, sửa, xóa thông tin hành khách
- Liên kết hành khách với vé

### Quản Lý Nhân Viên
- Quản lý tài khoản nhân viên
- Phân quyền (Admin/User)

### Báo Cáo Doanh Thu
- Báo cáo doanh thu theo tháng
- Báo cáo doanh thu theo năm
- Chi tiết doanh thu từng chuyến bay

### Quy Định
- Quản lý các quy định về chuyến bay
- Giới hạn số lượng sân bay trung gian
- Quy định thời gian dừng tối đa/tối thiểu

### Xác Thực
- Đăng nhập/Đăng xuất
- JWT Authentication
- Phân quyền theo vai trò

## 🛠 Công Nghệ Sử Dụng

- **Backend Framework**: Flask 3.1.1
- **Database**: MySQL (PyMySQL)
- **ORM**: SQLAlchemy 2.0.41
- **Authentication**: Flask-JWT-Extended 4.7.1
- **Migration**: Flask-Migrate 4.1.0
- **CORS**: flask-cors 6.0.1
- **API Documentation**: flask-swagger-ui 5.21.0
- **Scheduler**: APScheduler 3.11.0
- **Payment**: VNPay integration
- **Server**: Gunicorn

## 📦 Cài Đặt

### Yêu Cầu Hệ Thống

- Python 3.12+
- MySQL 8.0+
- pip

### Cài Đặt Dependencies

1. Clone repository:
```bash
git clone <repository-url>
cd airport
```

2. Tạo virtual environment:
```bash
python -m venv venv
```

3. Kích hoạt virtual environment:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. Cài đặt các package:
```bash
pip install -r requirements.txt
```

## ⚙️ Cấu Hình

1. Tạo file `.env` trong thư mục gốc:
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=airport
KEY=your_jwt_secret_key
```

2. Tạo database MySQL:
```sql
CREATE DATABASE airport CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Import dữ liệu mẫu từ thư mục `backup/`:

   **Cách 1: Import bằng dòng lệnh (Windows PowerShell):**
   ```powershell
   # Import tất cả các file SQL
   Get-ChildItem backup\*.sql | ForEach-Object {
       mysql -u your_username -p airport < $_.FullName
   }
   ```

   **Cách 2: Import từng file (Linux/Mac/Windows):**
   ```bash
   mysql -u your_username -p airport < backup/airport_sanbay.sql
   mysql -u your_username -p airport < backup/airport_hangve.sql
   mysql -u your_username -p airport < backup/airport_nhanvien.sql
   mysql -u your_username -p airport < backup/airport_chuyenbay.sql
   mysql -u your_username -p airport < backup/airport_chitiethangve.sql
   mysql -u your_username -p airport < backup/airport_chitietsanbaytrunggian.sql
   mysql -u your_username -p airport < backup/airport_hanhkhach.sql
   mysql -u your_username -p airport < backup/airport_vechuyenbay.sql
   mysql -u your_username -p airport < backup/airport_quydinh.sql
   mysql -u your_username -p airport < backup/airport_doanhthuthang.sql
   mysql -u your_username -p airport < backup/airport_chi_tiet_doanh_thu_thang.sql
   mysql -u your_username -p airport < backup/airport_doanhthunam.sql
   mysql -u your_username -p airport < backup/airport_alembic_version.sql
   ```

   **Cách 3: Sử dụng MySQL Workbench/phpMyAdmin:**
   - Mở MySQL Workbench hoặc phpMyAdmin
   - Chọn database `airport`
   - Import từng file SQL từ thư mục `backup/` theo thứ tự:
     1. `airport_sanbay.sql`
     2. `airport_hangve.sql`
     3. `airport_nhanvien.sql`
     4. `airport_quydinh.sql`
     5. `airport_chuyenbay.sql`
     6. `airport_chitiethangve.sql`
     7. `airport_chitietsanbaytrunggian.sql`
     8. `airport_hanhkhach.sql`
     9. `airport_vechuyenbay.sql`
     10. `airport_doanhthuthang.sql`
     11. `airport_chi_tiet_doanh_thu_thang.sql`
     12. `airport_doanhthunam.sql`
     13. `airport_alembic_version.sql`

## 🚀 Chạy Ứng Dụng

### Chạy Development Server

```bash
python run.py
```

Ứng dụng sẽ chạy tại: `http://localhost:5000`

### Chạy với Gunicorn (Production)

```bash
gunicorn -c gunicorn.conf.py "app:create_app()"
```

Ứng dụng sẽ chạy tại: `http://localhost:8000`

## 📁 Cấu Trúc Dự Án

```
airport/
├── app/
│   ├── __init__.py              # Khởi tạo Flask app
│   ├── config.py                # Cấu hình ứng dụng
│   ├── database.py              # Kết nối database
│   ├── extensions.py            # Extensions (db, jwt, cors, migrate)
│   ├── models/                  # SQLAlchemy models
│   │   ├── Chuyenbay.py
│   │   ├── SanBay.py
│   │   ├── VeChuyenBay.py
│   │   ├── HanhKhach.py
│   │   ├── NhanVien.py
│   │   ├── HangVe.py
│   │   ├── QuyDinh.py
│   │   └── ...
│   ├── routes/                  # API endpoints
│   │   ├── Chuyenbay.py
│   │   ├── SanBay.py
│   │   ├── VeChuyenBay.py
│   │   ├── HanhKhach.py
│   │   ├── NhanVien.py
│   │   ├── auth.py
│   │   └── ...
│   ├── services/                # Business logic
│   │   ├── Chuyenbay_service.py
│   │   ├── SanBay_service.py
│   │   ├── VeChuyenBay_service.py
│   │   └── ...
│   ├── utils/                   # Utility functions
│   │   ├── auth.py
│   │   ├── validators.py
│   │   └── ...
│   └── vnpay/                   # VNPay payment integration
│       ├── route.py
│       └── vnpay.py
├── db/                          # Database backup files
├── tests/                       # Test files
├── README/                      # Chi tiết API documentation
├── .env                         # Environment variables
├── requirements.txt             # Python dependencies
├── run.py                       # Entry point
├── gunicorn.conf.py            # Gunicorn configuration
├── Dockerfile                   # Docker image
├── compose.yaml                 # Docker Compose
└── README.md                    # This file
```

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/login` - Đăng nhập
- `POST /api/auth/logout` - Đăng xuất
- `GET /api/auth/check_login` - Kiểm tra trạng thái đăng nhập

### Chuyến Bay
- `POST /api/chuyenbay/add` - Thêm chuyến bay mới
- `GET /api/chuyenbay/<id>` - Lấy thông tin chuyến bay theo ID
- `GET /api/chuyenbay/search` - Tìm kiếm chuyến bay
- `PUT /api/chuyenbay/<id>` - Cập nhật chuyến bay
- `DELETE /api/chuyenbay/<id>` - Xóa chuyến bay

### Sân Bay
- `POST /api/sanbay/add` - Thêm sân bay
- `GET /api/sanbay` - Lấy danh sách sân bay
- `PUT /api/sanbay/<id>` - Cập nhật sân bay
- `DELETE /api/sanbay/<id>` - Xóa sân bay

### Vé Chuyến Bay
- `POST /api/vechuyenbay/add` - Đặt vé
- `GET /api/vechuyenbay/<id>` - Lấy thông tin vé
- `GET /api/vechuyenbay` - Lấy danh sách vé

### Hành Khách
- `POST /api/hanhkhach/add` - Thêm hành khách
- `GET /api/hanhkhach/<id>` - Lấy thông tin hành khách
- `PUT /api/hanhkhach/<id>` - Cập nhật hành khách

### Nhân Viên
- `POST /api/nhanvien/add` - Thêm nhân viên
- `GET /api/nhanvien` - Lấy danh sách nhân viên
- `PUT /api/nhanvien/<id>` - Cập nhật nhân viên

### Báo Cáo Doanh Thu
- `GET /api/doanhthuthang` - Báo cáo doanh thu theo tháng
- `GET /api/doanhthunam` - Báo cáo doanh thu theo năm
- `GET /api/chitietdoanhthuthang` - Chi tiết doanh thu tháng

### Quy Định
- `GET /api/quydinh` - Lấy quy định
- `PUT /api/quydinh` - Cập nhật quy định

### Thanh Toán
- `POST /api/vnpay/create_payment` - Tạo thanh toán VNPay
- `GET /api/vnpay/payment_return` - Xử lý kết quả thanh toán

> **Lưu ý**: Một số endpoint yêu cầu JWT authentication và quyền Admin. Xem chi tiết trong thư mục `README/`.

## 📚 Tài Liệu API

Tài liệu chi tiết cho từng module được lưu trong thư mục `README/`:
- `ChuyenBay_README.md` - Tài liệu API Chuyến Bay
- `VeChuyenBay_README.md` - Tài liệu API Vé
- `SanBay_README.md` - Tài liệu API Sân Bay
- `HanhKhach_README.md` - Tài liệu API Hành Khách
- `NhanVien_README.md` - Tài liệu API Nhân Viên
- `DoanhThuThang_README.md` - Tài liệu Báo Cáo Doanh Thu Tháng
- `DoanhThuNam_README.md` - Tài liệu Báo Cáo Doanh Thu Năm
- `QuyDinh_README.md` - Tài liệu API Quy Định
- `HangVe_README.md` - Tài liệu API Hạng Vé
- `ThanhToanVNPAY_README.md` - Tài liệu Thanh Toán VNPay
- `Authenticated_README.md` - Tài liệu Xác Thực

### Swagger UI

Sau khi chạy ứng dụng, truy cập Swagger UI tại:
```
http://localhost:5000/api/docs
```

## 🐳 Docker

### Build và chạy với Docker Compose

```bash
docker compose up --build
```

Ứng dụng sẽ chạy tại: `http://localhost:8000`

### Build Docker image

```bash
docker build -t airport-app .
```

### Chạy container

```bash
docker run -p 8000:8000 --env-file .env airport-app
```

Xem thêm chi tiết trong `README.Docker.md`.

## 🔧 Phát Triển

### Database Migrations

Tạo migration mới:
```bash
flask db migrate -m "Description"
```

Áp dụng migration:
```bash
flask db upgrade
```

### Chạy Tests

```bash
python -m pytest tests/
```

### Cấu Hình Gunicorn

File `gunicorn.conf.py` chứa cấu hình:
- `bind`: Địa chỉ và port (0.0.0.0:8000)
- `workers`: Số worker processes (4)
- `timeout`: Request timeout (120s)

### Scheduler

Hệ thống sử dụng APScheduler để chạy các tác vụ định kỳ (ví dụ: cập nhật báo cáo doanh thu hàng ngày).

## 📝 Ghi Chú

- Đảm bảo MySQL đang chạy trước khi khởi động ứng dụng
- JWT token có thời gian sống 100 giờ (có thể điều chỉnh trong `app/config.py`)
- Một số endpoint yêu cầu quyền Admin
- Database sử dụng UTF-8 encoding để hỗ trợ tiếng Việt

## 👥 Đóng Góp

Dự án này là đồ án môn học SE104. Mọi đóng góp và phản hồi đều được hoan nghênh!

## 📄 License

Dự án này được phát triển cho mục đích học tập.

---

**Lưu ý**: Đảm bảo cập nhật file `.env` với thông tin database và secret key của bạn trước khi chạy ứng dụng.

