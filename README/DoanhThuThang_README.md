G. Doanh thu tháng


1. Thêm doanh thu tháng   (CẦN ĐĂNG NHẬP)
# # link api: http://localhost:5000/api/doanhthuthang/add_or_update?thang={year}&nam={month}

methods = POST

NOTE: khi chạy thêm doanh thu tháng, sẽ tạo luôn chi tiết doanh thu tháng (Biểu mẫu 5.1), nhưng chưa tính tỉ lệ của doanh thu tháng trong biểu mẫu 5.2. Để tạo tỉ lệ của doanh thu tháng trong biểu mẫu 5.2 phải tạo doanh thu 5 hoặc update doanh thu năm

ví dụ:
# link api: http://localhost:5000/api/doanhthuthang/add_or_update?thang=4&nam=2025

dữ liệu trả về:
- {"message": "Thêm doanh thu tháng thành công!", "status": "success"}, 200
- {
    "message": "{Lỗi}",
    "status": "fail"
}



2. Xem danh sách doanh thu tháng (Biểu mẫu 5.2)  (CẦN ĐĂNG NHẬP)
# link api: http://localhost:5000/api/ds_doanhthuthang/get?nam={year}
methods = GET

ví dụ: 
# http://localhost:5000/api/ds_doanhthuthang/get?nam=2025

dữ liệu trả về:
- {
    "data": [
        {
            "Tile": 0.35,
            "Tong_doanh_thu": 4425000.0,
            "month": 6,
            "so_chuyen_bay": 8,
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



3. Xem chi tiết doanh thu tháng (Biểu mẫu 5.1)  (CẦN ĐĂNG NHẬP)

# http://localhost:5000/api/chitietdoanhthuthang/get?thang={month}&nam={year}

methods = GET

ví dụ:
# http://localhost:5000/api/chitietdoanhthuthang/get?thang=4&nam=2025
dữ liệu trả về:

- {
    "data": [
        {
            "Doanh_thu": 1500000.0,
            "Ma_chuyen_bay": 21,
            "So_ghe_dat": 3,
            "Ti_le": 0.34,
            "nam": 2025,
            "thang": 6
        },
        {
            "Doanh_thu": 2400000.0,
            "Ma_chuyen_bay": 23,
            "So_ghe_dat": 4,
            "Ti_le": 0.54,
            "nam": 2025,
            "thang": 6
        },
        {
            "Doanh_thu": 525000.0,
            "Ma_chuyen_bay": 7,
            "So_ghe_dat": 1,
            "Ti_le": 0.12,
            "nam": 2025,
            "thang": 6
        }
    ],
    "message": "Truy cập dữ liệu thành công",
    "status": "success"
}


- {
    "message": "{Lỗi}",
    "status": "fail"
}