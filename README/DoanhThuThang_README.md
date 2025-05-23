G. Doanh thu tháng


1. Thêm doanh thu tháng 
# http://localhost:5000/api/doanhthuthang/add?thang={month}&nam={year}

methods = POST

NOTE: khi chạy thêm doanh thu tháng, sẽ tạo luôn chi tiết doanh thu tháng (Biểu mẫu 5.1), nhưng chưa tính tỉ lệ của doanh thu tháng trong biểu mẫu 5.2. Để tạo tỉ lệ của doanh thu tháng trong biểu mẫu 5.2 phải tạo doanh thu 5 hoặc update doanh thu năm

ví dụ:
# http://localhost:5000/api/doanhthuthang/add?thang=4&nam=2025

dữ liệu trả về:
- {"message": "Thêm doanh thu tháng thành công!", "status": "success"}, 200
- {
    "message": "{Lỗi}",
    "status": "fail"
}



2. Xem danh sách doanh thu tháng (Biểu mẫu 5.2)
# link api: http://localhost:5000/api/ds_doanhthuthang/get?nam={year}
methods = GET

ví dụ: 
# http://localhost:5000/api/ds_doanhthuthang/get?nam=2025

dữ liệu trả về:
- {
    "data": [
        {
            "Tile": 0.758621,
            "Tong_doanh_thu": 3300000.0,
            "month": 4,
            "so_chuyen_bay": 6,
            "year": 2025
        },
        {
            "Tile": 0.241379,
            "Tong_doanh_thu": 1050000.0,
            "month": 5,
            "so_chuyen_bay": 2,
            "year": 2025
        }
    ],
    "message": "Lấy dữ liệu thành công",
    "status": "success"
}
- {
    "message": "{Lỗi}",
    "status": "fail"
}



3. Xem chi tiết doanh thu tháng (Biểu mẫu 5.1)

# http://localhost:5000/api/chitietdoanhthuthang/get?thang={month}&nam={year}

methods = GET

ví dụ:
# http://localhost:5000/api/chitietdoanhthuthang/get?thang=4&nam=2025
dữ liệu trả về:

- {
    "data": [
        {
            "Doanh_thu": 0.0,
            "Ma_chuyen_bay": 6,
            "So_ghe_dat": 0,
            "So_ghe_trong": 100,
            "Ti_le": 0.0,
            "nam": 2025,
            "thang": 4
        },
        {
            "Doanh_thu": 1650000.0,
            "Ma_chuyen_bay": 8,
            "So_ghe_dat": 3,
            "So_ghe_trong": 97,
            "Ti_le": 0.5,
            "nam": 2025,
            "thang": 4
        },
        {
            "Doanh_thu": 1650000.0,
            "Ma_chuyen_bay": 9,
            "So_ghe_dat": 3,
            "So_ghe_trong": 97,
            "Ti_le": 0.5,
            "nam": 2025,
            "thang": 4
        },
        {
            "Doanh_thu": 0.0,
            "Ma_chuyen_bay": 10,
            "So_ghe_dat": 0,
            "So_ghe_trong": 100,
            "Ti_le": 0.0,
            "nam": 2025,
            "thang": 4
        },
        {
            "Doanh_thu": 0.0,
            "Ma_chuyen_bay": 11,
            "So_ghe_dat": 0,
            "So_ghe_trong": 100,
            "Ti_le": 0.0,
            "nam": 2025,
            "thang": 4
        }
    ],
    "message": "Truy cập dữ liệu thành công",
    "status": "success"
}


- {
    "message": "{Lỗi}",
    "status": "fail"
}