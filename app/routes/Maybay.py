from flask import Blueprint
from library import *
from app.services.Maybay_service import add_Maybay, get_Maybay, get_Maybay_all, delete_Maybay, update_Maybay

MAYBAY = Blueprint('maybay', __name__)

@MAYBAY.route('/maybay/add', methods=['POST'])
def add_maybay_route():
    try:
        data = request.get_json()
        add_Maybay(data)
        return jsonify({'message': 'Máy bay đã được thêm'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
    

    
@MAYBAY.route('/maybay/get', methods=['GET'])
def get_maybay_route():
    try:
        maybay = get_Maybay_all()
        return jsonify(maybay)
    except ValueError as e:
        return jsonify({'message': str(e)}),400


@MAYBAY.route('/maybay/get/<int:id>', methods=['GET'])
def get_maybay_by_id_route(id):
    try:
        maybay = get_Maybay(id)
        return jsonify(maybay)
    except ValueError as e:
        return jsonify({'message': str(e)}), 400



@MAYBAY.route('/maybay/delete/<int:id>', methods=['DELETE'])
def delete_maybay_route(id):
    try:
        delete_Maybay(id)
        return jsonify({'message': 'Máy bay đã được xóa'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    
    
@MAYBAY.route('/maybay/update/<int:id>', methods=['PUT'])
def update_maybay_route(id):
    try:
        data = request.get_json()
        update_Maybay(id, data)
        return jsonify({'message': 'Máy bay đã được cập nhật'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    
