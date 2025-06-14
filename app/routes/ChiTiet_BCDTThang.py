from flask import Blueprint, request, jsonify
from app.services.ChiTietDoanhThuThang_service import (
    update_tile_Chitietdoanhthu_service,
    get_ds_chitietdoanhthu_service,
    create_or_update_chitietdoanhthuThang_service_bymonth
)
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin

CHITIETDOANHHTHUTHANG = Blueprint('ChiTietDoanhThuThang', __name__)




# link api: http://localhost:5000/api/chitietdoanhthuthang/update/tile?thang=4&nam=2025
@CHITIETDOANHHTHUTHANG.route('/chitietdoanhthuthang/update/tile', methods=['PUT'])
@jwt_required()
def update_tile_chitietdoanhthuthang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        if not thang or not nam:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm", "status": "fail"}), 400
        
        update_tile_Chitietdoanhthu_service(thang, nam, 3300000, 2)
        return jsonify({"message": "Cập nhật tỷ lệ chi tiết doanh thu tháng thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    




# link api: http://localhost:5000/api/chitietdoanhthuthang/get?thang=4&nam=2025

@CHITIETDOANHHTHUTHANG.route('/chitietdoanhthuthang/get', methods=['GET'])
@jwt_required()
def get_chitietdoanhthuthang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        if not thang or not nam:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm", "status": "fail"}), 400
        
        # Call the service to get the data
        ds_chitietdoanhthu = get_ds_chitietdoanhthu_service(thang, nam)
        
        # For demonstration purposes, returning a mock response
        
        
        return jsonify({'message': 'Truy cập dữ liệu thành công',
                        'data': [ctdt.serialize() for ctdt in ds_chitietdoanhthu],
                        'status': 'success'}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail" }), 500



# link api: http://localhost:5000/api/chitietdoanhthuthang/create_or_update_chitietdoanhthuThang?month=4&year=2025
@CHITIETDOANHHTHUTHANG.route('/chitietdoanhthuthang/create_or_update_chitietdoanhthuThang', methods=['POST'])
@jwt_required()
def create_or_update_chitietdoanhthuThang():
    try:
        month = request.args.get('month')
        year = request.args.get('year')
        if not month or not year:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm", "status": "fail"}), 400
        create_or_update_chitietdoanhthuThang_service_bymonth(month, year)
        return jsonify({"message": "Tạo hoặc cập nhật chi tiết doanh thu tháng thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
