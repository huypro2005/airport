from flask import Blueprint, request, jsonify
from app.services.NhanVien_service import add_nhanvien_service

NHANVIEN = Blueprint('nhanvien', __name__)

@NHANVIEN.route('/nhanvien/add', methods=['POST'])
def add_nhanvien_route():
    try:
        data = request.get_json()
        add_nhanvien_service(data)
        return jsonify({'message': 'Nhân viên đã được thêm'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500




