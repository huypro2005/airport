from flask import Blueprint, request, jsonify
from app.services.SanBay_service import add_SanBay_service, get_ds_sanbay_service, get_sanbay_by_id_service, delete_sanbay_service, update_sanbay_service
from flask_jwt_extended import jwt_required
from app.utils.auth import is_admin
SANBAY = Blueprint('sanbay', __name__)


'''
    {
        "Ma_san_bay": "HNOI",
        "Ten_san_bay": "Ha noi"
    }
    
'''
# link api: http://localhost:5000/api/sanbay/add
@SANBAY.route('/sanbay/add', methods=['POST'])
# @jwt_required()
def add_sanbay():
    try:
        data = request.get_json()
        
        add_SanBay_service(data)

        return jsonify({"message": "Sân bay đã được thêm thành công!", "status": "success"}), 201
    
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    
    
    


'''
    [
        {
            "Ma_san_bay": "HNOI",
            "Ten_san_bay": "Ha noi"
        },
        {
            "Ma_san_bay": "SGON",
            "Ten_san_bay": "Sai Gon"
        },
        {
            "Ma_san_bay": "DNANG",
            "Ten_san_bay": "Da Nang"
        }
    ]

'''
# link api: http://localhost:5000/api/sanbay/get
@SANBAY.route('/sanbay/get', methods=['GET'])
# @jwt_required()
def get_ds_sanbay():
    try:
        ds_sanbay = get_ds_sanbay_service()
        data = []
        for sanbay in ds_sanbay:
            data.append({
                'Ma_san_bay': sanbay.id,
                'Ten_san_bay': sanbay.ten_san_bay
            })
        return jsonify({"message": data, "status": "success"})    
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    

'''
    {
        "Ma_san_bay": "HNOI",
        "Ten_san_bay": "Ha noi"
    }
    
'''

@SANBAY.route('/sanbay/get/<string:id>', methods=['GET'])
@jwt_required()
def get_sanbay_by_id(id):
    try:
        sanbay = get_sanbay_by_id_service(id)
        return jsonify(sanbay)
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    


# link api: http://localhost:5000/api/sanbay/delete/<id>
@SANBAY.route('/sanbay/delete/<string:id>', methods=['DELETE'])
# @jwt_required
def delete_sanbay(id):
    try:
        delete_sanbay_service(id)
        return jsonify({"message": "Sân bay đã ngừng hoạt động!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    


# link api: http://localhost:5000/api/sanbay/update/<id>
@SANBAY.route('/sanbay/update/<string:id>', methods=['PUT'])
def update_sanbay(id):
    try:
        data = request.get_json()
        update_sanbay_service(id, data)
        return jsonify({"message": "Sân bay đã được cập nhật thành công!", "status": "success"}), 200
    except ValueError as e:
        return jsonify({"message": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"message": str(e), "status": "fail"}), 500
    


