from app.services.ChiTietSanBayTrungGian_service import get_ds_ChiTietSanBayTrungGian_service, update_Thoigiandung_CTSBTG_service
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin

CHITIETCHUYENBAY = Blueprint('ChiTietChuyenBay', __name__)


# link api: http://localhost:5000/api/chuyenbay/chitietchuyenbay/get/1
@CHITIETCHUYENBAY.route('/chuyenbay/chitietchuyenbay/get/<chuyenbay_id>', methods = ['GET'])
def get_chitietchuyenbays(chuyenbay_id):
    try:
        ds = get_ds_ChiTietSanBayTrungGian_service(chuyenbay_id)
        return jsonify({'status': 'success', 'data': ds}) , 200
    except Exception as e:
        return jsonify({'message': f'Error: {e}', 'status': 'fail'}), 400
    



# link api: http://localhost:5000/api/chuyenbay/chitietchuyenbay/update_Thoigiandung/1?Thoigiandung=20
@CHITIETCHUYENBAY.route('/chuyenbay/chitietchuyenbay/update_Thoigiandung/<id>', methods=['PUT'])
@jwt_required()
def update_Thoigiandung(id):
    try:
        data = request.args.get('Thoigiandung')
        thoi_gian_dung = int(data) if data else None
        if not thoi_gian_dung:
            return jsonify({'message': 'Vui lòng nhập thời gian dừng', 'status': 'fail'}), 400
        
        # Call the service to update the Thoi_gian_dung
        update_Thoigiandung_CTSBTG_service(id, thoi_gian_dung)
        
        return jsonify({'message': 'Cập nhật thời gian dừng thành công', 'status': 'success'}), 200
    
    except ValueError as e:
        return jsonify({'message': str(e), 'status': 'fail'}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', 'status': 'fail' }), 500
