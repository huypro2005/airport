E. Hành Khách

1. Thêm hành khách mới
# http://localhost:5000/api/hanhkhach/add
methods =POST

body = {
        "Hoten": "Nguyen Van A",
        "cmnd": "123456780",
        "sdt": "0909090909",
        "gioi_tinh": "Nam"
    }

dữ liệu trả về: 
- {
    "message": "Hanh khach da duoc them",
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}

2. Xem Thông tin hành khách thông qua id

# http://localhost:5000/api/hanhkhach/get/<int:id>
methods = POST

ví dụ:

# http://localhost:5000/api/hanhkhach/get/1
 
dữ liệu trả về:
- {
    "data": {
        "Hoten": "nguyen van a",
        "cmnd": "116468466314",
        "gioi_tinh": "Nam",
        "id": 1,
        "sdt": "24544346"
    },
    "message": "Lấy dữ liệu thành công", 
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}


