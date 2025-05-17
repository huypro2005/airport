from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from app.models.NhanVien import Nhanvien

def get_current_user():
    verify_jwt_in_request()
    data= get_jwt_identity()
    id = data['id']
    user = Nhanvien.query.get(id)
    return user

def get_current_user_id():
    verify_jwt_in_request()
    data= get_jwt_identity()
    id = data['id']
    return id

def role_required(allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user = get_current_user()
            if not user:
                return jsonify({"msg": "User not found"}), 404
                
            if user.pos not in allowed_roles:
                return jsonify({"msg": "Không có quyền truy cập"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

# Constants for roles

ROLE_ADMIN = 'admin'

def is_admin():
    return role_required([ROLE_ADMIN])

