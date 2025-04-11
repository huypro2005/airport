from flask import Blueprint
from library import *
from app.services.Maybay_service import add_Maybay, get_Maybay, get_Maybay_all, delete_Maybay, update_Maybay
# only admin can access
from app.utils.auth import is_admin, is_giamdoc
from flask_jwt_extended import jwt_required


MAYBAY = Blueprint('maybay', __name__)


# link api: http://localhost:5000/api/maybay/add
'''
{
    "ten_may_bay": "Boeing 737"
}
'''
@MAYBAY.route('/maybay/add', methods=['POST'])
@is_giamdoc()
@jwt_required()
def add_maybay_route():
    try:
        data = request.get_json()
        add_Maybay(data)
        return jsonify({'message': 'Máy bay đã được thêm'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
    


# link api: http://localhost:5000/api/maybay/get
@MAYBAY.route('/maybay/get', methods=['GET'])
@jwt_required()
def get_maybay_route():
    try:
        maybay = get_Maybay_all()
        return jsonify(maybay)
    except ValueError as e:
        return jsonify({'message': str(e)}),400


# link api: http://localhost:5000/api/maybay/get/<int:id>
@MAYBAY.route('/maybay/get/<int:id>', methods=['GET'])
@jwt_required()
def get_maybay_by_id_route(id):
    try:
        maybay = get_Maybay(id)
        return jsonify(maybay)
    except ValueError as e:
        return jsonify({'message': str(e)}), 400


# link api: http://localhost:5000/api/maybay/delete/<int:id>
@MAYBAY.route('/maybay/delete/<int:id>', methods=['DELETE'])
@is_giamdoc()
@jwt_required()
def delete_maybay_route(id):
    try:
        delete_Maybay(id)
        return jsonify({'message': 'Máy bay đã được xóa'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    

# link api: http://localhost:5000/api/maybay/update/<int:id>
'''
{
    "ten_may_bay": "Boeing 737"
}
'''
@MAYBAY.route('/maybay/update/<int:id>', methods=['PUT'])
@is_giamdoc()
@jwt_required()
def update_maybay_route(id):
    try:
        data = request.get_json()
        update_Maybay(id, data)
        return jsonify({'message': 'Máy bay đã được cập nhật'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    
