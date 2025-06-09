C. Chuyến Bay


1. Thêm chuyến bay mới

# http://localhost:5000/api/chuyenbay/add
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
- {
    "message": "Chuyến bay đã được thêm thành công!",
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}


2. Xem chuyến bay theo id chuyến bay
# http://localhost:5000/api/chuyenbay/get/<id>
method = POST

ví dụ:
# http://localhost:5000/api/chuyenbay/get/6

Dữ liệu trả về:
- {
    "data": {
        "Ma_chuyen_bay": 6,
        "Ma_san_bay_den": "SGON",
        "Ma_san_bay_di": "HNOI",
        "So_ghe_dat": 0,
        "So_ghe_trong": 100,
        "Thoi_gian_bay": 40,
        "chitiet_hangve": [
            {
                "Gia_ve": 1100000.0,
                "Ma_chuyen_bay": 6,
                "Ma_hang_ve": 1,
                "So_ve_da_dat": 0,
                "So_ve_trong": 50
            },
            {
                "Gia_ve": 1050000.0,
                "Ma_chuyen_bay": 6,
                "Ma_hang_ve": 2,
                "So_ve_da_dat": 0,
                "So_ve_trong": 50
            }
        ],
        "chitiet_sanbay_trung_gian": [],
        "gia_ve": 1000000.0,
        "gio_khoi_hanh": "00:00:00",
        "gio_toi": "00:40:00",
        "ngay_khoi_hanh": "2025-04-25",
        "ngay_toi": "2025-04-25"
    },
    "message": "Lấy dữ liệu thành công",
    "status": "success"
}

- {
    "message": "{Lỗi}",
    "status": "fail"
}


3. Xem chuyến bay trong khoảng thời gian, từ sân bay đi đến sân bay đến
# http://localhost:5000/api/chuyenbay/search?start_time={datetime}&end_time={datetime}&sanbay_di={from}&sanbay_den={to}

method = GET

time ở dạng ISO 8601 
ví dụ: 2026-04-25T23:59:59

# http://localhost:5000/api/chuyenbay/search?start_time=2025-04-20T00:00:00&end_time=2026-04-25T23:59:59&sanbay_di=HAIPHONG&sanbay_den=SGON

dữ liệu trả về:
- {
    "data": [
        {
            "Ma_chuyen_bay": 6,
            "Ma_san_bay_den": "SGON",
            "Ma_san_bay_di": "HNOI",
            "So_ghe_dat": 0,
            "So_ghe_trong": 100,
            "Thoi_gian_bay": 40,
            "chitiet_hangve": [
                {
                    "Gia_ve": 1100000.0,
                    "Ma_chuyen_bay": 6,
                    "Ma_hang_ve": 1,
                    "So_ve_da_dat": 0,
                    "So_ve_trong": 50
                },
                {
                    "Gia_ve": 1050000.0,
                    "Ma_chuyen_bay": 6,
                    "Ma_hang_ve": 2,
                    "So_ve_da_dat": 0,
                    "So_ve_trong": 50
                }
            ],
            "chitiet_sanbay_trung_gian": [],
            "gia_ve": 1000000.0,
            "gio_khoi_hanh": "00:00:00",
            "gio_toi": "00:40:00",
            "ngay_khoi_hanh": "2025-04-25",
            "ngay_toi": "2025-04-25"
        }
    ],
    "message": "Lấy danh sách chuyến bay thành công",
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}



4. Cập nhật chuyến bay

NOTE: chỉ có thể cập nhật ngày giờ bay, thời gian bay trên không và giá vé

# link api: http://localhost:5000/api/chuyenbay/update/<id>
methods = PUT

ví dụ:
# http://localhost:5000/api/chuyenbay/update/6

body = {
    "ngay_khoi_hanh": "2025-04-25",
    "gio_khoi_hanh": "00:00:00",
    "gia_ve": 1000000,
    "Thoi_gian_bay": 40,
    "chitiet":[
        {
            "Ma_san_bay_trung_gian": "DNANG",
            "thoigian_dung": 15,
            "ghichu": "Tg 1",
            "is_delete": 0
        },
        {
            "Ma_san_bay_trung_gian": "Vinh",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 2",
            "is_delete": 1
        }
    ]
}


dữ liệu trả về: 

- {
    "message": "Chuyến bay đã được cập nhật thành công!",
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}


5. Xóa chuyến bay
# link api: http://localhost:5000/api/chuyenbay/delete/<id>

methods = DELETE

ví dụ: http://localhost:5000/api/chuyenbay/delete/36

Dũ liệu trả về: 
- {
    "message": "Chuyến bay đã được xóa thành công!",
    "status": "success"
}
- {
    "message": "Không thể xóa chuyến bay đã có vé đặt",
    "status": "fail"
}
