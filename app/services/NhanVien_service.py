from app.utils.auth import get_current_user_id
from app.models.NhanVien import Nhanvien
from app.utils.validators import validate_NhanVien
from library import *


def add_nhanvien_service(data):
    validate_NhanVien(data)
    id = data['id']
    name = data['name']
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


    nhanvien = Nhanvien(id = id, name= name, username = username,
                         password = hash_password, email = email,
                         position = position)
    try:
        db.session.add(nhanvien)
        db.session.commit()
    except Exception as e:
        raise ValueError(f"Lỗi: {e}")



def update_TinhtrangNghi_service(id):
    try:
        nhanvien = Nhanvien.query.filter_by(id = id).first()
        if not nhanvien:
            raise ValueError("Nhân viên không tồn tại")
        nhanvien.tinhtrang = False
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi: {e}")
    

def get_all_nhanvien_service():
    try:
        id = get_current_user_id()
        nhanvien = Nhanvien.query.filter(Nhanvien.id != id).all()
        if not nhanvien:
            raise ValueError("Không có nhân viên nào")
        return nhanvien
    except Exception as e:
        raise ValueError(f"Lỗi: {e}")