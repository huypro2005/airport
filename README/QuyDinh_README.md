F. Quy định

1. Xem tất cả quy định  (CẦN ĐĂNG NHẬP)
# link api: http://localhost:5000/api/quydinh/get
methods = GET

dữ liệu trả về:
- {
    "data": {
        "soluongsanbaytrunggian": 3,
        "thoigianbaytoithieu": 10,
        "thoigiandatvetoithieu": 1,
        "thoigiandungtoida": 25,
        "thoigiandungtoithieu": 15,
        "thoigianhuyvetoida": 1
    },
    "message": "Lấy quy định thành công",
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}

2. cập nhật quy định  (CẦN ĐĂNG NHẬP)
# link api: http://localhost:5000/api/quydinh/update
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
- {
    'message': 'Cập nhật quy định thành công',
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}

