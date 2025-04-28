from app.models.NhanVien import Nhanvien
from app.utils.validators import validate_NhanVien
from library import *


def add_nhanvien_service(data):
    validate_NhanVien(data)
    id = data['id']
    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    password = data['password']
    email = data['email']
    position = data['position']

    hash_password = generate_password_hash(password)

    if Nhanvien.query.filter_by(username = username).first():
        raise ValueError("Tên tài khoản đã tồn tại")

    if Nhanvien.query.filter_by(email = email).first():
        raise ValueError("Email đã tồn tại")
    
    if Nhanvien.query.filter_by(id = id).first():
        raise ValueError("Mã nhân viên đã tồn tại")


    nhanvien = Nhanvien(id = id, first_name = first_name,
                         last_name = last_name, username = username,
                         password = hash_password, email = email,
                         position = position)
    try:
        db.session.add(nhanvien)
        db.session.commit()
    except Exception as e:
        raise ValueError(f"Lỗi: {e}")

