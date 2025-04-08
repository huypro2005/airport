from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from app.models.NhanVien import Nhanvien

def role_required(allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            user = Nhanvien.query.get(current_user_id)
            
            if not user:
                return jsonify({"msg": "User not found"}), 404
                
            if user.pos not in allowed_roles:
                return jsonify({"msg": "Không có quyền truy cập"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

# Constants for roles
ROLE_NHANVIEN = 0
ROLE_GIAMDOC = 1
ROLE_ADMIN = 2

def is_giamdoc():
    return role_required([ROLE_GIAMDOC])

def is_admin():
    return role_required([ROLE_ADMIN])

def is_nhanvien():
    return role_required([ROLE_NHANVIEN, ROLE_GIAMDOC, ROLE_ADMIN])