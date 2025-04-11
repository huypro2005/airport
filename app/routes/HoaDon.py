from flask import Blueprint, request, jsonify, session
from app.services.HoaDon_service import create_hoadon_service
from flask_jwt_extended import jwt_required
from app.utils.auth import get_current_user_id


HOADON = Blueprint('hoadon', __name__)


# link api: http://localhost:5000/api/hoadon/add
'''
{
    "Ma_hanh_khach": 1,
    "Ma_ve_cb": 1
    "Thanh_tien": 1000000,
    "Ghi_chu": "Ghi chú"
}

'''
@HOADON.route('/hoadon/add', methods=['POST'])
@jwt_required()
def add_hoadon_route():
    try:
        data = request.get_json()
        nhanvien_id = get_current_user_id()
        create_hoadon_service(data, nhanvien_id)
        return jsonify({'message': 'Hóa đơn đã được thêm'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
