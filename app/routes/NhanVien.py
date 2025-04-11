from flask import Blueprint, request, jsonify
from app.services.NhanVien_service import add_nhanvien_service
from app.utils.auth import is_admin
from flask_jwt_extended import jwt_required

NHANVIEN = Blueprint('nhanvien', __name__)

@NHANVIEN.route('/nhanvien/add', methods=['POST'])
@jwt_required()
@is_admin()
def add_nhanvien_route():
    
    '''
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "username": "john.doe",
        "password": "password123",
        "email": "john.doe@example.com",
        "pos": 0,
        "position": "admin"
    }
    '''
    
    try:
        data = request.get_json()
        add_nhanvien_service(data)
        return jsonify({'message': 'Nhân viên đã được thêm'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500




