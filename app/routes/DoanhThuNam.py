from flask import Blueprint, request, jsonify
from app.services.DoanhThuNam_service import create_or_update_doanhthu_nam_service, update_doanhthu_nam_service
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin

DOANHTHUNAM = Blueprint('doanhthu_nam', __name__)

# link api: http://localhost:5000/api/doanhthunam/add_or_update?nam=2025
@DOANHTHUNAM.route('/doanhthunam/add_or_update', methods=['POST'])
def add_or_update_doanhthu_nam():
    try:
        nam = request.args.get('nam')
        if not nam:
            return jsonify({"message": "Thiếu thông tin năm", "status": "fail"}), 400
        create_or_update_doanhthu_nam_service(nam)
        return jsonify({"message": "Thêm doanh thu năm thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    

# link api: http://localhost:5000/api/doanhthunam/update?nam=2025
@DOANHTHUNAM.route('/doanhthunam/update', methods=['PUT'])
def update_doanhthu_nam():
    try:
        nam = request.args.get('nam')
        if not nam:
            return jsonify({"message": "Thiếu thông tin năm", "status": "fail"}), 400
        update_doanhthu_nam_service(nam)
        return jsonify({"message": "Cập nhật doanh thu năm thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500