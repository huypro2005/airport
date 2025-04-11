from app.services.PhieuDatCho_service import add_phieudatcho, Thanhtoan_phieudatcho_services
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
PHIEUDATCHO = Blueprint('phieudatcho', __name__)


@PHIEUDATCHO.route('/phieudatcho/add', methods=['POST'])
@jwt_required()
def add_phieudatcho_route():
    try:
        data = request.get_json()
        add_phieudatcho(data)
        return jsonify({'message': 'Thêm phiếu đặt chỗ thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Lỗi không xác định'}), 500
    

@PHIEUDATCHO.route('/phieudatcho/thanhtoan/<int:id>', methods=['POST'])
@jwt_required()
def thanhtoan_phieudatcho_route(id):
    try:
        Thanhtoan_phieudatcho_services(id)
        return jsonify({'message': 'Thanh toán phiếu đặt chỗ thành công'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500
        
