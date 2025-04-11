from flask import Blueprint, request, jsonify
from library import *
from app.models.NhanVien import Nhanvien
from app.services.auth_service import login_service, logout_service

AUTH = Blueprint('auth', __name__)

@AUTH.route('/login', methods = ['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if not username or not password:
            return jsonify({'message': 'Vui lòng nhập tên tài khoản và mật khẩu'}), 400
        result = login_service(username, password)
        return jsonify(result), 200
        
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@AUTH.route('/logout', methods = ['POST'])
def logout():
    return logout_service()

