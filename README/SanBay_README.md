B. Sân bay


1. Thêm sân bay mới
# http://localhost:5000/api/sanbay/add
method = POST
 
body = {
        "Ma_san_bay": "HNOI",
        "Ten_san_bay": "Ha noi"
    }

dữ liệu trả về:

- {
    "message": "Sân bay đã được thêm thành công!",
    "status": "success"
}


- {
    "message": "{Lỗi}",
    "status": "fail"
}


2. Xem tất cả các sân bay
# link api: http://localhost:5000/api/sanbay/get
method = GET

dữ liệu trả về:

- {
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
    ],
    "status": "success"
}


- {
    "message": "{Lỗi}",
    "status": "fail"
}