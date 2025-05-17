from flask import Blueprint, request, jsonify
from app.services.DoanhThuNam_service import create_doanhthu_nam_service, update_doanhthu_nam_service
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin

DOANHTHUNAM = Blueprint('doanhthu_nam', __name__)

# link api: http://localhost:5000/api/doanhthunam/add?nam=2025
@DOANHTHUNAM.route('/doanhthunam/add', methods=['POST'])
def add_doanhthu_nam():
    try:
        nam = request.args.get('nam')
        if not nam:
            return jsonify({"message": "Thiếu thông tin năm"}), 400
        create_doanhthu_nam_service(nam)
        return jsonify({"message": "Thêm doanh thu năm thành công!"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

# link api: http://localhost:5000/api/doanhthunam/update?nam=2025
@DOANHTHUNAM.route('/doanhthunam/update', methods=['PUT'])
def update_doanhthu_nam():
    try:
        nam = request.args.get('nam')
        if not nam:
            return jsonify({"message": "Thiếu thông tin năm"}), 400
        update_doanhthu_nam_service(nam)
        return jsonify({"message": "Cập nhật doanh thu năm thành công!"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500