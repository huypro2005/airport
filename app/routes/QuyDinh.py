from app.services.QuyDinh_service import update_quydinh_soLuongSanBay, update_quydinh_thoiGianBayToiThieu, update_quydinh_soLuongSanBayTrungGian, update_quydinh_thoiGianDungToiThieu, update_quydinh_thoiGianDungToiDa, update_quydinh_phanTramGiaVeHang1, update_quydinh_phanTramGiaVeHang2, update_quydinh_thoiGianDatVeToiDa
from flask import Blueprint
from flask import request, jsonify

QUYDINH = Blueprint('quydinh', __name__)

@QUYDINH.route('/quydinh/update/soLuongSanBay', methods=['PUT'])
def update_soLuongSanBay():
    try:    
        data = request.get_json()
        update_quydinh_soLuongSanBay(data)
        return jsonify({'message': 'Cập nhật quy định số lượng sân bay thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500


@QUYDINH.route('/quydinh/update/thoiGianBayToiThieu', methods=['PUT'])
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
def update_phanTramGiaVeHang2():
    try:
        data = request.get_json()
        update_quydinh_phanTramGiaVeHang2(data)
        return jsonify({'message': 'Cập nhật quy định phần trăm giảm giá vé hàng 2 thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
    






