from app.services.HanhKhach_service import add_hanh_khach, get_hanh_khach_by_id
from flask import Blueprint
from library import *

HANHKHACH = Blueprint('hanhkhach', __name__)

@HANHKHACH.route('/hanhkhach/add', methods=['POST'])
def add_hanh_khach_route():
    try:
        data = request.json
        add_hanh_khach(data)
        return jsonify({'message': 'Hanh khach da duoc them'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500


@HANHKHACH.route('/hanhkhach/get/<int:id>', methods=['GET'])
def get_hanh_khach(id):
    try:
        hanh_khach = get_hanh_khach_by_id(id)
        return jsonify(hanh_khach)
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500





