from app.services.HangVe_service import add_hangve_service, get_ds_HangVe_service
from flask import Blueprint, request, jsonify

HANGVE = Blueprint('hangve', __name__)

# link api: http://localhost:5000/api/hangve/add
'''
    {
        "Ten_hang_ve": "Hang 1",
        "Ti_le_don_gia": 1.05
    }
'''

@HANGVE.route('/hangve/add', methods = ['POST'])
def add_hangve():
    try:
        data = request.get_json()
        add_hangve_service(data)
        return jsonify({"message": "Thêm hạng vé thành công!"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


# link api: http://localhost:5000/api/hangve/get
@HANGVE.route('/hangve/get', methods = ['GET'])
def get_hangve():
    try:
        hangve = get_ds_HangVe_service()
        if not hangve:
            return jsonify({"message": "Không có hạng vé nào!"}), 404
        # data = []
        # for hv in hangve:
        #     data.append({
        #         "id": hv.id,
        #         "Ten_hang_ve": hv.Ten_hang_ve,
        #         "Ti_le_don_gia": hv.Ti_le_don_gia
        #     })
        return jsonify({"message": [hv.serialize() for hv in hangve]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500