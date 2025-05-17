from flask import Blueprint, request, jsonify
from app.services.DoanhThuThang_service import create_doanhthu_thang_service, get_ds_doanhthuthang_service
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin

DOANHTHUTHANG = Blueprint('doanhthu_thang', __name__)


# link api: http://localhost:5000/api/doanhthuthang/add?thang=4&nam=2025
@DOANHTHUTHANG.route('/doanhthuthang/add', methods=['POST'])
def add_doanhthu_thang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        if not thang or not nam:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm"}), 400
        create_doanhthu_thang_service(thang, nam)
        return jsonify({"message": "Thêm doanh thu tháng thành công!"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    



# link api: http://localhost:5000/api/ds_doanhthuthang/get?nam=2025
@DOANHTHUTHANG.route('/ds_doanhthuthang/get', methods=['GET'])
def get_doanhthu_thang():
    try:
        nam = request.args.get('nam')
        if  not nam:
            return jsonify({"message": "Thiếu thông tin tháng hoặc năm"}), 400
        doanhthu_thang = get_ds_doanhthuthang_service(nam)
        if not doanhthu_thang:
            return jsonify({"message": "Không có doanh thu tháng nào!"}), 404
        return jsonify({"message": 'Lấy dữ liệu thành công','data': [dt.serialize() for dt in doanhthu_thang]}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500