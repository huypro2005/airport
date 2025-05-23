K. Nhân viên

1. Thêm mới nhân viên

# link api: http://localhost:5000/api/nhanvien/add
methods = POST

    
    '''
    {
        "id": 2,
        "name": "John Doe",
        "username": "john.doe",
        "password": "password123",
        "email": "john.doe@example.com",
        "position": "admin"
    }
    '''


dữ liệu trả về:

- {'message': 'Nhân viên đã được thêm', "status": "success"}
- {
    "message": "{Lỗi}",
    "status": "fail"
}



2. Cập nhật tình trạng nghỉ việc

# http://localhost:5000/api/nhanvien/update_tinhtrangnghi/<int:id>

methods = PUT

ví dụ: 