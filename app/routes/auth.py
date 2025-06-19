from flask import Blueprint, request, jsonify
from library import *
from app.models.NhanVien import Nhanvien
from app.services.auth_service import login_service, logout_service, jwt_required, get_jwt_identity, get_jwt

AUTH = Blueprint('auth', __name__)


'''
{
    "username": "john.doe",
    "password": "password123"
}
'''
# link api: http://localhost:5000/api/auth/login
@AUTH.route('/auth/login', methods = ['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        if not username or not password:
            return jsonify({'message': 'Vui lòng nhập tên tài khoản và mật khẩu', 'status': 'fail'}), 400
        result = login_service(username, password)
        return jsonify({'status': 'success', 'data': result}), 200
        
    except ValueError as e:
        return jsonify({'message': str(e), 'status': 'fail'}), 400
    except Exception as e:
        return jsonify({'message': str(e), 'status': 'fail'}), 500
    
@AUTH.route('/auth/logout', methods = ['POST'])
def logout():
    return logout_service()


# Kiểm tra trạng thái đăng nhập
# link api: http://localhost:5000/api/auth/check_login
@AUTH.route('/auth/check_login', methods=['GET'])
@jwt_required()  # Yêu cầu JWT hợp lệ
def check_login():
    current_user = get_jwt_identity()
    # lấy thông tin additional_claims từ JWT
    claims = get_jwt()
    
    user = Nhanvien.query.get(current_user)
    return jsonify({
        "status": "success",
        "userID": user.id,
        "additional_claims": claims
    }), 200