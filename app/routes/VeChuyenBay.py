from flask import Blueprint, request, jsonify
from app.services.VeChuyenBay_service import (add_veChuyenyBay_service, 
                                              get_veChuyenBay_byID_service, 
                                               delete_ve_service,
                                               update_ve_vitri_ghe_service,
                                                get_ds_veChuyenBay_da_dat_hom_nay_service,
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
@jwt_required()
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
 

 
# link api: http://localhost:5000/api/vechuyenbay/delete/<int:id>

@VECHUYENBAY.route('/vechuyenbay/delete/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_ve(id):
    try:
        delete_ve_service(id)
        return jsonify({'message': 'Xóa vé thành công', "status": "success"}), 200
    except ValueError as e:
        return jsonify({'message': str(e), "status": "fail"}), 400



# link api: http://localhost:5000/api/vechuyenbay/get_by_hanhkhach/cmnd/<string:hk_cccd>

@VECHUYENBAY.route('vechuyenbay/get_by_hanhkhach/cmnd/<string:hk_cmnd>', methods=['GET'])
@jwt_required()
def get_ve_by_hanh_khach(hk_cmnd):
    try:
        ve_list = get_ds_veChuyenBay_by_HanhKhach_service(hk_cmnd)
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
        
        return jsonify({'message': 'Lấy vé thành công', 'data': result, "status": "success", 'id_hanhkhach': ve_list[0].Ma_hanh_khach}), 200
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', "status": "fail"}), 500



# link api: http://localhost:5000/api/vechuyenbay/update/vitriGhe/<int:id>
@VECHUYENBAY.route('vechuyenbay/update/vitriGhe/<int:id>', methods=['PUT'])
@jwt_required()
def update_vitri_ghe(id):
    data = request.get_json()
    try:
        update_ve_vitri_ghe_service(id, data)
        return jsonify({'message': 'Cập nhật vị trí ghế thành công', 'status': 'success'}), 200
    except ValueError as e:
        return jsonify({'message': str(e), 'status': 'fail'}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', 'status': 'fail'}), 500
    

# link api: http://localhost:5000/api/vechuyenbay/get/DatHomNay
@VECHUYENBAY.route('vechuyenbay/get/DatHomNay', methods=['GET'])
@jwt_required()
def get_ds_veChuyenBay_da_dat_hom_nay():
    try:
        ds_ve = get_ds_veChuyenBay_da_dat_hom_nay_service()
        if not ds_ve:
            return jsonify({'message': 'Không có vé nào đã đặt trong ngày hôm nay', "status": "success"}), 200
        
        result = []
        for ve in ds_ve:
            result.append({
                'Ma_ve': ve.id,
                'Ma_chuyen_bay': ve.Ma_chuyen_bay,
                'Ma_hang_ve': ve.Ma_hang_ve,
                'vi_tri': ve.vi_tri,
                'Tien_ve': ve.Tien_ve,
                'Ma_hanh_khach': ve.Ma_hanh_khach
            })
        
        return jsonify({'message': 'Lấy vé thành công', 'data': result, "status": "success"}), 200
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', "status": "fail"}), 500