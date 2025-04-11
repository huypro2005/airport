from flask import Blueprint, request, jsonify
from app.services.SanBay_service import add_SanBay_service, get_ds_sanbay_service, get_sanbay_by_id_service, delete_sanbay_service, update_sanbay_service
from flask_jwt_extended import jwt_required
from app.utils.auth import is_giamdoc
SANBAY = Blueprint('sanbay', __name__)

@SANBAY.route('/sanbay/add', methods=['POST'])
@jwt_required()
@is_giamdoc()
def add_sanbay():
    try:
        data = request.get_json()
        
        add_SanBay_service(data)

        return jsonify({"message": "Sân bay đã được thêm thành công!"}), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    


@SANBAY.route('/sanbay/get', methods=['GET'])
@jwt_required()
def get_ds_sanbay():
    try:
        ds_sanbay = get_ds_sanbay_service()
        data = []
        for sanbay in ds_sanbay:
            data.append({
                'Ma_san_bay': sanbay.id,
                'Ten_san_bay': sanbay.ten_san_bay
            })
        return jsonify(data)    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@SANBAY.route('/sanbay/get/<int:id>', methods=['GET'])
@jwt_required()
def get_sanbay_by_id(id):
    try:
        sanbay = get_sanbay_by_id_service(id)
        return jsonify(sanbay)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@SANBAY.route('/sanbay/delete/<int:id>', methods=['DELETE'])
@jwt_required()
@is_giamdoc()
def delete_sanbay(id):
    try:
        delete_sanbay_service(id)
        return jsonify({"message": "Sân bay đã được xóa thành công!"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@SANBAY.route('/sanbay/update/<int:id>', methods=['PUT'])
def update_sanbay(id):
    try:
        data = request.get_json()
        update_sanbay_service(id, data)
        return jsonify({"message": "Sân bay đã được cập nhật thành công!"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    




