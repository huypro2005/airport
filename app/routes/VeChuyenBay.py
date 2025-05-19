from flask import Blueprint, request, jsonify
from app.services.VeChuyenBay_service import (add_veChuyenyBay_service, 
                                              get_veChuyenBay_byID_service, 
                                               delete_ve_service,
                                               get_ds_veChuyenBay_by_HanhKhach_service)
from flask_jwt_extended import jwt_required

VECHUYENBAY = Blueprint('vechuyenbay', __name__)



'''

    {
        "Ma_chuyen_bay": 1,
        "Ma_hang_ve": 1,
        "vitri": "B4.1",
        "Ho_ten": "nguyen van a",
        "cmnd": "116468466314",
        "sdt": "24544346",
        "gioi_tinh": "Nam"
    }

'''
# link api: http://localhost:5000/api/vechuyenbay/add
@VECHUYENBAY.route('/vechuyenbay/add', methods=['POST'])
# @jwt_required()
def add_ve():
    data = request.get_json()
    try:
        ve = add_veChuyenyBay_service(data)
        res = {
            'Ma_ve': ve.id,
            'Ma_chuyen_bay': ve.Ma_chuyen_bay,
            'hang_ve': ve.Ma_hang_ve,
            'vi_tri': ve.vi_tri,
            'Ma_hanh_khach': ve.Ma_hanh_khach,
            'Tien_ve': ve.Tien_ve
        }
        return jsonify({'message': 'Đặt vé thành công', 've': res, "status": "success"}), 200
    except ValueError as e:
        return jsonify({'message': str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi server: {e}', "status": "fail"}), 500





# link api: http://localhost:5000/api/vechuyenbay/get/<int:id>
@VECHUYENBAY.route('/vechuyenbay/get/<int:id>', methods=['GET'])
# @jwt_required()
def get_ve_chuyen_bay(id):
    try:
        result = get_veChuyenBay_byID_service(id)
        if result:
            data = {
                'Ma_chuyen_bay': result.Ma_chuyen_bay,
                'Ma_hang_ve': result.Ma_hang_ve,
                'vi_tri': result.vi_tri,
                'Ma_hanh_khach': result.Ma_hanh_khach
            }
            return jsonify({'message': 'Lấy dữ liệu thành công', 
                            'data': data, "status": "success"}), 200
        else:
            return jsonify({'message': 'Không tìm thấy vé', "status": "fail"}), 404
    except ValueError as e:
        return jsonify({'message': str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', "status": "fail"}), 500
 

# @VECHUYENBAY.route('/vechuyenbay/update/hangve', methods=['PUT'])
# # @jwt_required()
# def update_hangve():
#     try:
#         id = request.args.get('id')
#         hangve = request.args.get('hangve')
#         update_ve_Hangve_service(id, hangve)
#         return jsonify({'message': 'Cập nhật hàng vé thành công'}), 200
#     except ValueError as e:
#         return jsonify({'message': str(e)}), 400
#     except Exception as e:
#         return jsonify({'message': f'Lỗi: {e}'}), 500
        

# @VECHUYENBAY.route('/vechuyenbay/huyve/<id>', methods = ['PUT'])
# def update_huyVeChuyenBay(id):
#     try:
#         update_huy_ve_service(id)
#         return jsonify({'message': 'Hủy vé thành công'}), 200
#     except ValueError as e:
#         return jsonify({'message': str(e)}), 400
#     except Exception as e:
#         return jsonify({'message': f'Lỗi: {e}'}), 500

@VECHUYENBAY.route('/vechuyenbay/delete/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_ve(id):
    try:
        delete_ve_service(id)
        return jsonify({'message': 'Xóa vé thành công', "status": "success"}), 200
    except ValueError as e:
        return jsonify({'message': str(e), "status": "fail"}), 400



# link api: http://localhost:5000/api/vechuyenbay/get_by_hanhkhach/<int:hk_id>

@VECHUYENBAY.route('vechuyenbay/get_by_hanhkhach/<int:hk_id>', methods=['GET'])
# @jwt_required()
def get_ve_by_hanh_khach(hk_id):
    try:
        ve_list = get_ds_veChuyenBay_by_HanhKhach_service(hk_id)
        if not ve_list:
            return jsonify({'message': 'Không tìm thấy vé cho hành khách này', "status": "fail"}), 404
        
        result = []
        for ve in ve_list:
            result.append({
                'Ma_ve': ve.id,
                'Ma_chuyen_bay': ve.Ma_chuyen_bay,
                'Ma_hang_ve': ve.Ma_hang_ve,
                'vi_tri': ve.vi_tri,
                'Tien_ve': ve.Tien_ve
            })
        
        return jsonify({'message': 'Lấy vé thành công', 'data': result, "status": "success"}), 200
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', "status": "fail"}), 500
