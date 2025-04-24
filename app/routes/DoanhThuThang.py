from flask import Blueprint, request, jsonify
from app.services.DoanhThuThang_service import create_doanhthu_thang_service, get_doanhthu_thang_service, get_doanh_thu_chuyenbay_all_by_thang_service, get_BaoCaoDoanhThuNam_service
from flask_jwt_extended import jwt_required

DOANHTHUTHANG = Blueprint('doanhthu_thang', __name__)



# link api: http://localhost:5000/api/doanhthu_thang/add?thang=1&nam=2024
@DOANHTHUTHANG.route('/doanhthu_thang/add', methods=['POST'])
# @jwt_required()
def add_doanhthu_thang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        doanhthu = create_doanhthu_thang_service(thang, nam)
        data = {
            'thang': doanhthu.month,
            'nam': doanhthu.year,
            'doanhthu': doanhthu.Tong_doanh_thu,
            'chuyenbay': doanhthu.so_chuyen_bay,
        }
        return jsonify({'message': 'Doanh thu tháng đã được tạo thành công', 'data': data}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Lỗi server'}), 500


# link api: http://localhost:5000/api/doanhthu_thang/get?thang=1&nam=2024
@DOANHTHUTHANG.route('/doanhthu_thang/get', methods=['GET'])    
# @jwt_required()
def get_doanhthu_thang():
    try:
        thang = request.args.get('thang')
        nam = request.args.get('nam')
        doanhthu = get_doanhthu_thang_service(thang, nam)
        data = {
            'thang': doanhthu.month,
            'nam': doanhthu.year,
            'doanhthu': doanhthu.Tong_doanh_thu,
            'chuyenbay': doanhthu.so_chuyen_bay
        }
        return jsonify({'message': 'Doanh thu tháng đã được tạo thành công', 'data': data}), 200    
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Lỗi server'}), 500
    

# link api: http://localhost:5000/api/doanhthu_thang/get/chuyenbay?thang=1&nam=2024
@DOANHTHUTHANG.route('/doanhthu_thang/get/chuyenbay', methods=['GET'])
# @jwt_required()
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


# link api: http://localhost:5000/api/doanhthu_thang/get/baocaodoanhthunam?nam=2024
@DOANHTHUTHANG.route('/doanhthu_thang/get/baocaodoanhthunam', methods=['GET'])
# @jwt_required()
def get_baocaodoanhthunam():
    try:
        nam = request.args.get('nam')
        baoCao = get_BaoCaoDoanhThuNam_service(nam)
        return jsonify({'message': 'Báo cáo doanh thu năm đã được tạo thành công', 'data': baoCao}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': f'Lỗi: {e}'}), 500

