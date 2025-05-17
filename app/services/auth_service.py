from app import jwt
from flask_jwt_extended import create_refresh_token, create_access_token, get_jwt_identity, jwt_required
from app.models.NhanVien import Nhanvien
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify

def authenticate(username, password):
    user = Nhanvien.query.filter(Nhanvien.username==username, Nhanvien.tinhtrang == 1).first()
    if not user:
        raise ValueError("Tên tài khoản không tồn tại")
    if not check_password_hash(user.password, password):
        raise ValueError("Mật khẩu không chính xác")
    return user


def login_service(username, password):
    user = authenticate(username, password)
    data = {
        'username': user.username,
        'id': user.id,
    }
    access_token = create_access_token(identity=data)
    refresh_token = create_refresh_token(identity=data)
    return {
        'access_token': access_token,
        'refresh_token': refresh_token, 
        'username': user.username,
        'position': user.position,
        'id': user.id
    }

def logout_service():
    return jsonify({'message': 'Đăng xuất thành công'}), 200






