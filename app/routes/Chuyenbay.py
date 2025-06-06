from app.services.Chuyenbay_service import (add_ChuyenBay_service, 
                    get_chuyenbay_byID_service, get_dsChuyenBay_follow_time_service, 
                    update_chuyenbay_thoigianbay_service,
                    update_chuyenbay_ngaygiobay_service,
                    get_Chuyenbay_by_thang_service,
                    update_chuyenbay_service)
from flask import Blueprint, request, jsonify
from app.models.Chuyenbay import Chuyenbay
from app.models.SanBay import Sanbay
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin
CHUYENBAY = Blueprint('chuyennbay', __name__)

# link api: http://localhost:5000/api/chuyenbay/add
'''
    {
    "Ma_chuyen_bay": 10,
    "Ma_san_bay_di": "HNOI",
    "Ma_san_bay_den": "SGON",
    "gia_ve": 500000,
    "ngay_khoi_hanh": "2025-05-25",
    "gio_khoi_hanh": "00:00:00",
    "thoi_gian_bay": 30,
    "chitiet":[
        {
            "Ma_san_bay_trung_gian": "DNANG",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 1"
        },
        {
            "Ma_san_bay_trung_gian": "Vinh",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 2"
        }
    ],
    "hangve": [
        {
            "Ma_hang_ve": 1,
            "So_ghe_trong_hang": 50
        },
        {
            "Ma_hang_ve": 2,
            "So_ghe_trong_hang": 50
        }
    ]
}    


'''

@CHUYENBAY.route('/chuyenbay/add', methods=['POST'])
# @jwt_required()
# cần payload truyền vào
def add_chuyenbay():
    try:
        data = request.get_json()
        add_ChuyenBay_service(data)

        return jsonify({"message": "Chuyến bay đã được thêm thành công!", "status": "success"}), 201
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    
    
    

# link api: http://localhost:5000/api/chuyenbay/get/<id>

@CHUYENBAY.route('/chuyenbay/get/<id>', methods=['GET'])
def get_chuyenbay_byID(id):
    try:
        chuyenbay = get_chuyenbay_byID_service(id)
        
        return jsonify({"message": "Lấy dữ liệu thành công", 'data': chuyenbay, "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 404
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    
    

# link api: http://localhost:5000/api/chuyenbay/search?start_time=2025-04-20T00:00:00&end_time=2026-04-25T23:59:59&sanbay_di=HAIPHONG&sanbay_den=SGON

@CHUYENBAY.route('/chuyenbay/search', methods=['GET'])
def get_dsChuyenBay_follow_time():
    try:
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        sanbay_di = request.args.get('sanbay_di')
        sanbay_den = request.args.get('sanbay_den')
        
        if not all([start_time, end_time, sanbay_di, sanbay_den]):
            return jsonify({
                "message": "Thiếu thông tin tìm kiếm",
                "status": "fail"
            }), 400
            
        dsChuyenBay = get_dsChuyenBay_follow_time_service(start_time, end_time, sanbay_di, sanbay_den)
        
        return jsonify({
            "message": "Lấy danh sách chuyến bay thành công",
            "status": "success",
            "data": dsChuyenBay
        }), 200
        
    except ValueError as e:
        return jsonify({
            "message": str(e),
            "status": "fail"
        }), 400
    except Exception as e:
        return jsonify({
            "message": str(e),
            "status": "fail"
        }), 500
    


# link api: http://localhost:5000/api/chuyenbay/update_thoigianbay/<id>?thoigianbay=30

@CHUYENBAY.route('/chuyenbay/update_thoigianbay/<id>', methods=['PUT'])
def update_thoigianbay(id):
    try:
        thoigianbay = request.args.get('thoigianbay')
        update_chuyenbay_thoigianbay_service(id, thoigianbay)
        return jsonify({"message": "Thời gian bay đã được cập nhật thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    

# link api: http://localhost:5000/api/chuyenbay/update_thoigianbay/<id>?thoigianbay=2025-04-25T00:00:00

@CHUYENBAY.route('/chuyenbay/update_ngaygiobay/<id>', methods= ['PUT'])
def update_ngaygiobay(id):
    try:
        ngaygiobay = request.args.get('ngaygiobay')
        update_chuyenbay_ngaygiobay_service(id, ngaygiobay)
        return jsonify({"message": "Ngày giờ bay đã được cập nhật thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500



# link api: http://localhost:5000/api/chuyenbay/update/<id>


@CHUYENBAY.route('/chuyenbay/update/<id>', methods=['PUT'])
def update_chuyenbay(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Không có dữ liệu để cập nhật'}), 400
        update_chuyenbay_service(id, data)
        
        return jsonify({"message": "Chuyến bay đã được cập nhật thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    


# link api: http://localhost:5000/api/chuyenbay/get/by_month?month=4&year=2025
@CHUYENBAY.route('/chuyenbay/get/by_month', methods = ['GET'])
def get_chuyenbay_by_month():
    try:
        month = request.args.get('month')
        year = request.args.get('year')
        if not month or not year:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm", "status": "fail"}), 400
        chuyenbay = get_Chuyenbay_by_thang_service(month, year)
        if not chuyenbay:
            return jsonify({"message": "Không có chuyến bay nào trong tháng này", "status": "fail"}), 404
        return jsonify({"message": [cb.serialize() for cb in chuyenbay], "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    

# link api: http://localhost:5000/api/chuyenbay/get/all
@CHUYENBAY.route('/chuyenbay/get/all', methods=['GET'])
def get_all_chuyenbay_service():
    try:
        chuyenbay = get_all_chuyenbay_service()
        if not chuyenbay:
            return jsonify({"message": "Không có chuyến bay nào", "status": "fail"}), 404
        return jsonify({"message": [cb.serialize() for cb in chuyenbay], "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500