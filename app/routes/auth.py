from flask import Blueprint, request, jsonify
from library import *
from app.models.NhanVien import Nhanvien

AUTH = Blueprint('auth', __name__)

@AUTH.route('/login', methods = ['POST'])
def login():
    try:
        data = request.get_json()
        if not data or not data['username'] or not data['password']:
            return jsonify({'message': 'Vui lòng nhập tên tài khoản và mật khẩu'}), 400
        
        nhanvien = Nhanvien.query.filter_by(username = data['username']).first()
        if not nhanvien:
            return jsonify({'message': 'Tên tài khoản không tồn tại'}), 400
    except:
        pass            
