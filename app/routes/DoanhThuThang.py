from flask import Blueprint, request, jsonify
from app.services.DoanhThuThang_service import create_doanhthu_thang_service, get_doanhthu_thang_service, get_doanh_thu_chuyenbay_all_by_thang_service

DOANHTHUTHANG = Blueprint('doanhthu_thang', __name__)

@DOANHTHUTHANG.route('/doanhthu_thang/add', methods=['POST'])
def add_doanhthu_thang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        doanhthu = create_doanhthu_thang_service(thang, nam)
        data = {
            'thang': doanhthu.month,
            'nam': doanhthu.year,
            'doanhthu': doanhthu.Tong_doanh_thu
        }
        return jsonify({'message': 'Doanh thu tháng đã được tạo thành công', 'data': data}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Lỗi server'}), 500



@DOANHTHUTHANG.route('/doanhthu_thang/get', methods=['GET'])
def get_doanhthu_thang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        doanhthu = get_doanhthu_thang_service(thang, nam)
        data = {
            'thang': doanhthu.month,
            'nam': doanhthu.year,
            'doanhthu': doanhthu.Tong_doanh_thu
        }
        return jsonify({'message': 'Doanh thu tháng đã được tạo thành công', 'data': data}), 200    
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Lỗi server'}), 500
    

    
@DOANHTHUTHANG.route('/doanhthu_thang/get/chuyenbay', methods=['GET'])
def get_doanhthu_thang_chuyenbay():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        doanhthu = get_doanh_thu_chuyenbay_all_by_thang_service(thang, nam)
        return jsonify({'message': 'Doanh thu tháng đã được tạo thành công', 'data': doanhthu}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500

