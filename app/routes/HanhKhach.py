from app.services.HanhKhach_service import add_hanh_khach, get_hanh_khach_by_id
from flask import Blueprint
from library import *
from flask_jwt_extended import jwt_required

HANHKHACH = Blueprint('hanhkhach', __name__)

# link api: http://localhost:5000/api/hanhkhach/add
'''
    {
        "Hoten": "Nguyen Van A",
        "cmnd": "123456780",
        "sdt": "0909090909",
        "gioi_tinh": "Nam"
    }
'''
@HANHKHACH.route('/hanhkhach/add', methods=['POST'])
# @jwt_required()
def add_hanh_khach_route():
    try:
        data = request.get_json()
        add_hanh_khach(data)
        return jsonify({'message': 'Hanh khach da duoc them'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500


# link api: http://localhost:5000/api/hanhkhach/get/<int:id>
@HANHKHACH.route('/hanhkhach/get/<int:id>', methods=['GET'])
# @jwt_required()
def get_hanh_khach(id):
    try:
        hanh_khach = get_hanh_khach_by_id(id)
        return jsonify({'message': 'Lấy dữ liệu thành công', 
                            'data': hanh_khach.serialize()}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500





