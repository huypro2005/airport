SE104

28/4/2025: có thêm tháng, năm ở phần chi tiết doanh thu, mn sửa lại cơ sở dữ liệu bằng cách:
vào mysql -> drop database airport -> create database airport -> chạy lại code python -> hoàn thành


Các api cần thiết:
- Tạo sân bay
- Tạo chuyến bay
- Tạo hành khách
- Tạo vé chuyến bay


Cách chạy chương trình:
B1: download python trên vs code
B2: pip install -r requirements.txt
B3: Tạo database airport trong mysql
    create database airport
B4: vào ./app/config.py sửa dòng 6 theo dạng
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{password}@localhost:3306/airport?charset=utf8mb4'
B5: chạy terminal: cd tới thư mục chưa file run.py
    chạy lệnh: python run.py



API chưa có :
- tìm khách hàng theo cccd, sdt
API cải thiện :
- doanh thu tháng năm sẽ phải xem lại





















