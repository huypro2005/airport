from flask import Blueprint, request, jsonify, session
from app.services.HoaDon_service import create_hoadon_service


HOADON = Blueprint('hoadon', __name__)

@HOADON.route('/hoadon/add', methods=['POST'])

def add_hoadon_route():
    try:
        data = request.get_json()
        create_hoadon_service(data, session['nhanvien_id'])
        return jsonify({'message': 'Hóa đơn đã được thêm'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
