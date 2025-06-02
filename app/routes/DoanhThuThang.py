from flask import Blueprint, request, jsonify
from app.services.DoanhThuThang_service import create_or_update_doanhthu_thang_service, get_ds_doanhthuthang_service
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin

DOANHTHUTHANG = Blueprint('doanhthu_thang', __name__)


# link api: http://localhost:5000/api/doanhthuthang/add_or_update?thang=4&nam=2025
@DOANHTHUTHANG.route('/doanhthuthang/add_or_update', methods=['POST'])
def add_or_update_doanhthu_thang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        if not thang or not nam:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm", "status": "fail"}), 400
        create_or_update_doanhthu_thang_service(thang, nam)
        return jsonify({"message": "Thêm doanh thu tháng thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    



# link api: http://localhost:5000/api/ds_doanhthuthang/get?nam=2025
@DOANHTHUTHANG.route('/ds_doanhthuthang/get', methods=['GET'])
def get_doanhthu_thang():
    try:
        nam = request.args.get('nam')
        if  not nam:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm", "status": "fail"}), 400
        doanhthu_thang = get_ds_doanhthuthang_service(nam)
        if not doanhthu_thang:
            return jsonify({"message": "Không có doanh thu tháng nào!", "status": "fail"}), 404
        return jsonify({"message": 'Lấy dữ liệu thành công','data': [dt.serialize() for dt in doanhthu_thang], "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500