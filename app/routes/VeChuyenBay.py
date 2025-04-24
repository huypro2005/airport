from flask import Blueprint, request, jsonify
from app.services.VeChuyenBay_service import (add_veChuyenyBay_service, 
                                              get_veChuyenBay_byID_service, 
                                              update_ve_Hangve_service,
                                               delete_ve_service, 
                                               update_huy_ve_service)
from flask_jwt_extended import jwt_required

VECHUYENBAY = Blueprint('vechuyenbay', __name__)



'''

    {
        "Ma_chuyen_bay": 1,
        "hang_ve": 1,
        "vitri": "B4.1",
        "Ho_ten": "nguyen van a",
        "cmnd": "116468466314",
        "sdt": "24544346",
        "gioi_tinh": "Nam"
    }

'''
@VECHUYENBAY.route('/vechuyenbay/add', methods=['POST'])
# @jwt_required()
def add_ve():
    data = request.get_json()
    try:
        ve = add_veChuyenyBay_service(data)
        res = {
            'Ma_ve': ve.id,
            'Ma_chuyen_bay': ve.Ma_chuyen_bay,
            'hang_ve': ve.hang_ve,
            'vi_tri': ve.vi_tri,
            'Ma_hanh_khach': ve.Ma_hanh_khach,
            'Tien_ve': ve.Tien_ve
        }
        return jsonify({'message': 'Đặt vé thành công', 've': res}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Lỗi server'}), 500





@VECHUYENBAY.route('/vechuyenbay/get/<int:id>', methods=['GET'])
# @jwt_required()
def get_ve_chuyen_bay(id):
    try:
        result = get_veChuyenBay_byID_service(id)
        if result:
            data = {
                'Ma_chuyen_bay': result.Ma_chuyen_bay,
                'hang_ve': result.hang_ve,
                'vi_tri': result.vi_tri,
                'Ma_hanh_khach': result.Ma_hanh_khach
            }
            return jsonify(data), 200
        else:
            return jsonify({'message': 'Không tìm thấy vé'}), 404
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
 

@VECHUYENBAY.route('/vechuyenbay/update/hangve', methods=['PUT'])
# @jwt_required()
def update_hangve():
    try:
        id = request.args.get('id')
        hangve = request.args.get('hangve')
        update_ve_Hangve_service(id, hangve)
        return jsonify({'message': 'Cập nhật hàng vé thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
        

@VECHUYENBAY.route('/vechuyenbay/huyve/<id>', methods = ['PUT'])
def update_huyVeChuyenBay(id):
    try:
        update_huy_ve_service(id)
        return jsonify({'message': 'Hủy vé thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500

@VECHUYENBAY.route('/vechuyenbay/delete/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_ve(id):
    try:
        delete_ve_service(id)
        return jsonify({'message': 'Xóa vé thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
