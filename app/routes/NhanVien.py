from flask import Blueprint, request, jsonify
from app.services.NhanVien_service import add_nhanvien_service, update_TinhtrangNghi_service
from app.utils.auth import is_admin
from flask_jwt_extended import jwt_required

NHANVIEN = Blueprint('nhanvien', __name__)


# link api: http://localhost:5000/api/nhanvien/add
@NHANVIEN.route('/nhanvien/add', methods=['POST'])
# @jwt_required()
# @is_admin()
def add_nhanvien_route():
    
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
    
    try:
        data = request.get_json()
        add_nhanvien_service(data)
        return jsonify({'message': 'Nhân viên đã được thêm', "status": "success"}), 201
    except ValueError as e:
        return jsonify({'message': str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', "status": "fail"}), 500



# link api: http://localhost:5000/api/nhanvien/update_tinhtrangnghi/<int:id>
@NHANVIEN.route('/nhanvien/update_tinhtrangnghi/<int:id>', methods=['PUT'])
@jwt_required()
@is_admin()
def update_tinhtrangnghi_route(id):
    try:
        update_TinhtrangNghi_service(id)
        return jsonify({'message': 'Cập nhật tình trạng nghỉ thành công', "status": "success"}), 200
    except ValueError as e:
        return jsonify({'message': str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', "status": "fail"}), 500

