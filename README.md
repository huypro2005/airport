SE104

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
B5: vào ./app/config.py sửa dòng 6 theo dạng
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{password}@localhost:3306/airport?charset=utf8mb4'
B5: chạy terminal: cd tới thư mục chưa file run.py
    chạy lệnh: python run.py

Các api đã hoàn thiện:


A. Hạng vé

1. Tạo hạng vé
link api: http://localhost:5000/api/hangve/add 
body={
        "Ten_hang_ve": "Hang 1",
        "Ti_le_don_gia": 1.05
    }

method = POST

dữ liệu trả về:
- "message": "Thêm hạng vé thành công!", 201
- "error": "{Lỗi}", 400
- "error": "{Lỗi}", 500



2. Xem tất cả hạng vé
link api: http://localhost:5000/api/hangve/get
method = GET

dữ liệu trả về:
- {
    "message": [
        {
            "Ten_hang_ve": "Hang 1",
            "Ti_le_don_gia": 1.05,
            "id": 1
        },
        {
            "Ten_hang_ve": "Hang 2",
            "Ti_le_don_gia": 1.0,
            "id": 2
        }
    ]
}

- "error": "{Lỗi}", 400
- "error": "{Lỗi}", 500


B. Sân bay


1. Thêm sân bay mới
http://localhost:5000/api/sanbay/add
method = POST
 
body = {
        "Ma_san_bay": "HNOI",
        "Ten_san_bay": "Ha noi"
    }

dữ liệu trả về:

- {"message": "Sân bay đã được thêm thành công!"}
- "error": "{Lỗi}", 400
- "error": "{Lỗi}", 500


2. Xem tất cả các sân bay
link api: http://localhost:5000/api/sanbay/get
method = GET

dữ liệu trả về:

{
    "message": [
        {
            "Ma_san_bay": "DNANG",
            "Ten_san_bay": "Da Nang"
        },
        {
            "Ma_san_bay": "HNOI",
            "Ten_san_bay": "Ha noi"
        },
        {
            "Ma_san_bay": "VINH",
            "Ten_san_bay": "Nghe An"
        },
        {
            "Ma_san_bay": "SGON",
            "Ten_san_bay": "Sai Gon"
        }
    ]
}



C. Chuyến Bay


1. Thêm chuyến bay mới

http://localhost:5000/api/chuyenbay/add
body = {
    "Ma_chuyen_bay": 6,
    "Ma_san_bay_di": "HNOI",
    "Ma_san_bay_den": "SGON",
    "gia_ve": 500000,
    "ngay_khoi_hanh": "2025-04-25",
    "gio_khoi_hanh": "00:00:00",
    "thoi_gian_bay": 30,
    "chitiet":[
        {
            "Ma_san_bay_trung_gian": "DNANG",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 1"
        },
        {
            "Ma_san_bay_trung_gian": "Vinh",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 2"
        }
    ],
    "hangve": [
        {
            "Ma_hang_ve": 1,
            "So_ghe_trong_hang": 50
        },
        {
            "Ma_hang_ve": 2,
            "So_ghe_trong_hang": 50
        }
    ]
}    

method = POST
  
dữ liệu trả về:
- "message": "Chuyến bay đã được thêm thành công!", 200
- "error" : "{Lỗi}", 400
- "error" : "{Lỗi}", 500


2. Xem chuyến bay theo id chuyến bay
http://localhost:5000/api/chuyenbay/get/<id>
method = POST

ví dụ:
http://localhost:5000/api/chuyenbay/get/6

Dữ liệu trả về:
- {
    "message": {
        "Ma_chuyen_bay": 6,
        "Ma_san_bay_den": "SGON",
        "Ma_san_bay_di": "HNOI",
        "Thoi_gian_bay": 30,
        "gia_ve": 500000.0,
        "gio_khoi_hanh": "00:00:00",
        "ngay_khoi_hanh": "2025-04-25"
    }
}


- "error" : "{Lỗi}", 400
- "error" : "{Lỗi}", 500


3. Xem chuyến bay trong khoảng thời gian 
http://localhost:5000/api/chuyenbay/search?start_time={datetime}&end_time={datetime}

method = GET

time ở dạng ISO 8601 
ví dụ: 2026-04-25T23:59:59

http://localhost:5000/api/chuyenbay/search?start_time=2025-04-20T00:00:00&end_time=2026-04-25T23:59:59

dữ liệu trả về:
- {
    "message": [
        {
            "Ma_chuyen_bay": 6,
            "Ma_san_bay_den": "SGON",
            "Ma_san_bay_di": "HNOI",
            "Thoi_gian_bay": 30,
            "gia_ve": 500000.0,
            "gio_khoi_hanh": "00:00:00",
            "ngay_khoi_hanh": "2025-04-25"
        },
        {
            "Ma_chuyen_bay": 7,
            "Ma_san_bay_den": "SGON",
            "Ma_san_bay_di": "VINH",
            "Thoi_gian_bay": 30,
            "gia_ve": 500000.0,
            "gio_khoi_hanh": "00:00:00",
            "ngay_khoi_hanh": "2025-05-25"
        }
    ]
}
- "error" : "{Lỗi}", 400
- "error" : "{Lỗi}", 500



C. Vé chuyến bay

1. Thêm vé chuyến bay 
http://localhost:5000/api/vechuyenbay/add
methods = POST
body = {
        "Ma_chuyen_bay": 1,
        "Ma_hang_ve": 1,
        "vitri": "B4.1",
        "Ho_ten": "nguyen van a",
        "cmnd": "116468466314",
        "sdt": "24544346",
        "gioi_tinh": "Nam"
    }
 

dữ liệu trả về:

- {
    "message": "Đặt vé thành công",
    "ve": {
        "Ma_chuyen_bay": 7,
        "Ma_hanh_khach": 4,
        "Ma_ve": 2,
        "Tien_ve": 525000.0,
        "hang_ve": 1,
        "vi_tri": "B4.12"
    }
}

- {'message' : '{lỗi}'}
- {'message' : 'Lỗi server: {e}'}


2. Xem chuyến bay theo id chuyến bay
http://localhost:5000/api/vechuyenbay/get/<int:id>
methods = GET
ví dụ:

http://localhost:5000/api/vechuyenbay/get/1

dữ liệu trả về:
- {
    "data": {
        "Ma_chuyen_bay": 7,
        "Ma_hang_ve": 1,
        "Ma_hanh_khach": 1,
        "vi_tri": "B4.1"
    },
    "message": "Lấy dữ liệu thành công"
}, 200

- {
    "message": "Không tìm thấy vé"
}

- {'message': '{Lỗi}'}
- {'message': 'Lỗi: {lỗi}'}



E. Hành Khách

1. Thêm hành khách mới
http://localhost:5000/api/hanhkhach/add
methods =POST

body = {
        "Hoten": "Nguyen Van A",
        "cmnd": "123456780",
        "sdt": "0909090909",
        "gioi_tinh": "Nam"
    }

dữ liệu trả về: 
- {
    "message": "Hanh khach da duoc them"
}
- {'message': '{Lỗi}'}
- {'message': 'Lỗi: {lỗi}'}


2. Xem Thông tin hành khách thông qua id

http://localhost:5000/api/hanhkhach/get/<int:id>
methods = POST

ví dụ:

http://localhost:5000/api/hanhkhach/get/1
 
dữ liệu trả về:
- {
    "data": {
        "Hoten": "nguyen van a",
        "cmnd": "116468466314",
        "gioi_tinh": "Nam",
        "id": 1,
        "sdt": "24544346"
    },
    "message": "Lấy dữ liệu thành công"
}
- {'message': '{Lỗi}'}
- {'message': 'Lỗi: {lỗi}'}

F. Quy định

1. Xem tất cả quy định
link api: http://localhost:5000/api/quydinh/get
methods = GET

dữ liệu trả về:
- {
    "data": {
        "soluongsanbaytrunggian": 3,
        "thoigianbaytoithieu": 10,
        "thoigiandatvetoithieu": 1,
        "thoigiandungtoida": 25,
        "thoigiandungtoithieu": 15
    },
    "message": "Lấy quy định thành công"
}
- {'message': '{lỗi}'}

2. cập nhật quy định
link api: http://localhost:5000/api/quydinh/update
methods = PUT

body = {
        "soluongsanbaytrunggian": 2,
        "thoigianbaytoithieu": 30,
        "thoigiandungtoida": 20,
        "thoigiandungtoithieu": 10,
        "thoigianvechuyenbay": 1
}

NOTE: cần thay đổi dữ liệu nào thì thay đổi dữ liệu đó, các dữ liệu còn lại thì điền mặc định là dữ liệu gốc lấy ở xem tất cả quy định

dữ liệu trả về:
- 'message': 'Cập nhật quy định thành công'
- {'message': '{Lỗi}'}
- {'message': 'Lỗi: {lỗi}'}