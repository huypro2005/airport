from app.services.HangVe_service import add_hangve_service, get_ds_HangVe_service, update_hangve_service
from flask import Blueprint, request, jsonify
from app.utils.auth import is_admin
from flask_jwt_extended import jwt_required

HANGVE = Blueprint('hangve', __name__)

# link api: http://localhost:5000/api/hangve/add
'''
    {
        "Ten_hang_ve": "Hang 1",
        "Ti_le_don_gia": 1.05
    }
'''

@HANGVE.route('/hangve/add', methods = ['POST'])
# @jwt_required()
def add_hangve():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Thiếu thông tin hạng vé!", "status": "fail"}), 400
        add_hangve_service(data)
        return jsonify({"message": "Thêm hạng vé thành công!", "status": "success"}), 201
    except ValueError as e:
        return jsonify({"error": str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({"error": str(e), "status": "fail"}), 500
    


# link api: http://localhost:5000/api/hangve/get

@HANGVE.route('/hangve/get', methods = ['GET'])
# @jwt_required()
def get_hangve():
    try:
        hangve = get_ds_HangVe_service()
        if not hangve:
            return jsonify({"message": "Không có hạng vé nào!", "status": "fail"}), 404
        # data = []
        # for hv in hangve:
        #     data.append({
        #         "id": hv.id,
        #         "Ten_hang_ve": hv.Ten_hang_ve,
        #         "Ti_le_don_gia": hv.Ti_le_don_gia
        #     })
        return jsonify({"message": [hv.serialize() for hv in hangve], "status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e), "status": "fail"}), 500
    


'''
        {
            "Ten_hang_ve": "Hang 1",
            "Ti_le_don_gia": 1.1
        }

'''

# link api: http://localhost:5000/api/hangve/update/<id>
@HANGVE.route('/hangve/update/<id>', methods=['PUT'])
def update_hangve(id):
    try:
        data = request.get_json()
        
        # Call the service to update the hang ve
        update_hangve_service(id, data)
        return jsonify({'message': 'Cập nhật hạng vé thành công', "status": "success"}), 200
    except ValueError as e:
        return jsonify({'message': str(e), "status": "fail"}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}', "status": "fail"}), 500