H. Doanh thu năm

1. Tạo doanh thu năm

# link api: http://localhost:8000/api/doanhthunam/add_or_update?nam=2025

methods = POST

ví dụ:
# link api: http://localhost:8000/api/doanhthunam/add_or_update?nam=2025

dữ liệu trả về: 

- {"message": "Thêm doanh thu năm thành công!", "status": "success"}
- {
    "message": "{Lỗi}",
    "status": "fail"
}





2. Cập nhật doanh thu năm (Không cần dùng)
# link api: http://localhost:5000/api/doanhthunam/update?nam={year}

methods = PUT


ví dụ: 

# link api: http://localhost:5000/api/doanhthunam/update?nam=2025

dữ liệu trả về:
- {"message": "Cập nhật doanh thu năm thành công!", "status": "success"}
- {
    "message": "{Lỗi}",
    "status": "fail"
}
