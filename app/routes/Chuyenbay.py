from app.services.Chuyenbay_service import add_ChuyenBay_service, get_chuyenbay_byID_service, get_dsChuyenBay_follow_time_service, update_chuyenbay_thoigianbay_service
from flask import Blueprint, request, jsonify
from app.models.Chuyenbay import Chuyenbay
from app.models.SanBay import Sanbay
CHUYENBAY = Blueprint('chuyennbay', __name__)

# link api: http://localhost:5000/api/chuyenbay/add
'''
    {
    "Ma_chuyen_bay": 6,
    "Ma_san_bay_di": 1,
    "Ma_san_bay_den": 2,
    "Ma_may_bay": 1,
    "gia_ve": 500000,
    "ngay_gio": "2024-04-25T10:30:00",
    "thoi_gian_bay": 30,
    "so_ghe_hang1": 15,
    "so_ghe_hang2": 20,
    "chitiet":[
        {
            "Ma_san_bay_trung_gian": 3,
            "thoigian_dung": 15,
            "ghichu": "Trung gian 1"
        },
        {
            "Ma_san_bay_trung_gian": 4,
            "thoigian_dung": 20,
            "ghichu": "Trung gian 2"
        }
    ]
}    


'''

@CHUYENBAY.route('/chuyenbay/add', methods=['POST'])
# cần payload truyền vào
def add_chuyenbay():
    try:
        data = request.get_json()
        add_ChuyenBay_service(data)

        return jsonify({"message": "Chuyến bay đã được thêm thành công!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

# link api: http://localhost:5000/api/chuyenbay/get/<id>

@CHUYENBAY.route('/chuyenbay/get/<id>', methods=['GET'])
def get_chuyenbay_byID(id):
    try:
        chuyenbay = get_chuyenbay_byID_service(id)
        data = {
            "Ma_chuyen_bay": chuyenbay.id,
            "Ma_san_bay_di": chuyenbay.Ma_san_bay_di,
            "Ma_san_bay_den": chuyenbay.Ma_san_bay_den,
            "Ma_may_bay": chuyenbay.Ma_may_bay,
            "ngay_gio": chuyenbay.ngay_gio.strftime('%Y-%m-%dT%H:%M:%S'),
            "Thoi_gian_bay": chuyenbay.Thoi_gian_bay
        }
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    

# link api: http://localhost:5000/api/chuyenbay/search?start_time=2024-04-25T10:30:00&end_time=2024-04-25T11:30:00

@CHUYENBAY.route('/chuyenbay/search', methods=['GET'])
def get_dsChuyenBay_follow_time():
    try:
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        dsChuyenBay = get_dsChuyenBay_follow_time_service(start_time, end_time)
        data = []
        for cb in dsChuyenBay:
            sanbaydi = Sanbay.query.get(cb.Ma_san_bay_di)
            sanbayden = Sanbay.query.get(cb.Ma_san_bay_den)
            item = {}
            item['Ma_chuyen_bay'] = cb.id
            item['San_bay_di'] = sanbaydi.ten_san_bay
            item['San_bay_den'] = sanbayden.ten_san_bay
            item['ngay_gio'] = cb.ngay_gio
            item['Thoi_gian_bay'] = cb.Thoi_gian_bay
            item['So_ghe_trong_hang1'] = cb.so_ghe_hang1
            item['So_ghe_trong_hang2'] = cb.so_ghe_hang2
            item['So_ghe_da_dat'] = cb.tong_so_ghe - cb.so_ghe_hang1 - cb.so_ghe_hang2
            data.append(item)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# link api: http://localhost:5000/api/chuyenbay/update_thoigianbay/<id>?thoigianbay=30

@CHUYENBAY.route('/chuyenbay/update_thoigianbay/<id>', methods=['PUT'])
def update_thoigianbay(id):
    try:
        thoigianbay = request.args.get('thoigianbay')
        update_chuyenbay_thoigianbay_service(id, thoigianbay)
        return jsonify({"message": "Thời gian bay đã được cập nhật thành công!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
