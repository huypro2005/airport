from app.services.QuyDinh_service import (update_quydinh_thoiGianBayToiThieu, 
                                          update_quydinh_soLuongSanBayTrungGian, update_quydinh_thoiGianDungToiThieu, 
                                          update_quydinh_thoiGianDungToiDa, update_quydinh_phanTramGiaVeHang1, 
                                          update_quydinh_phanTramGiaVeHang2, update_quydinh_thoiGianDatVeToiDa,
                                          get_quydinh)
from flask import Blueprint
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import is_giamdoc

QUYDINH = Blueprint('quydinh', __name__)


@QUYDINH.route('/quydinh/get', methods=['GET'])
# @jwt_required()
def get_quydinh():
    try:
        quydinh = get_quydinh()
        return jsonify({'message': 'Lấy quy định thành công', 'data': quydinh}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400



@QUYDINH.route('/quydinh/update/thoiGianBayToiThieu', methods=['PUT'])
# @jwt_required()
# @is_giamdoc()
def update_thoiGianBayToiThieu():
    try:
        data = request.get_json()
        update_quydinh_thoiGianBayToiThieu(data)
        return jsonify({'message': 'Cập nhật quy định thời gian bay tối thiểu thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500


@QUYDINH.route('/quydinh/update/soLuongSanBayTrungGian', methods=['PUT'])
# @jwt_required()
# @is_giamdoc()
def update_soLuongSanBayTrungGian():
    try:
        data = request.get_json()
        update_quydinh_soLuongSanBayTrungGian(data)
        return jsonify({'message': 'Cập nhật quy định số lượng sân bay trung gian thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500


@QUYDINH.route('/quydinh/update/thoiGianDungToiThieu', methods=['PUT'])
# @jwt_required()
# @is_giamdoc()
def update_thoiGianDungToiThieu():
    try:
        data = request.get_json()
        update_quydinh_thoiGianDungToiThieu(data)
        return jsonify({'message': 'Cập nhật quy định thời gian dừng tối thiểu thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500



@QUYDINH.route('/quydinh/update/thoiGianDungToiDa', methods=['PUT'])
# @jwt_required()
# @is_giamdoc()
def update_thoiGianDungToiDa():
    try:
        data = request.get_json()
        update_quydinh_thoiGianDungToiDa(data)
        return jsonify({'message': 'Cập nhật quy định thời gian dừng tối đa thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
    


@QUYDINH.route('/quydinh/update/phanTramGiaVeHang1', methods=['PUT'])
# @jwt_required()
# @is_giamdoc()
def update_phanTramGiaVeHang1():
    try:
        data = request.get_json()
        update_quydinh_phanTramGiaVeHang1(data)
        return jsonify({'message': 'Cập nhật quy định phần trăm giảm giá vé hàng 1 thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
    


@QUYDINH.route('/quydinh/update/phanTramGiaVeHang2', methods=['PUT'])
# @jwt_required()
# @is_giamdoc()
def update_phanTramGiaVeHang2():
    try:
        data = request.get_json()
        update_quydinh_phanTramGiaVeHang2(data)
        return jsonify({'message': 'Cập nhật quy định phần trăm giảm giá vé hàng 2 thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
    



@QUYDINH.route('/quydinh/update/thoiGianDatVeToiDa', methods=['PUT'])
# @jwt_required()
# @is_giamdoc()
def update_thoiGianDatVeToiDa():
    try:
        data = request.get_json()
        update_quydinh_thoiGianDatVeToiDa(data)
        return jsonify({'message': 'Cập nhật quy định thời gian đặt vé tối đa thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
    




