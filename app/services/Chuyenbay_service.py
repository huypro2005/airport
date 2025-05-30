from app.models.ChiTietHangVe import ChiTietHangVe
from app.models.Chuyenbay import Chuyenbay
from app.models.ChiTietSanBayTrungGian import ChiTietSanBayTrungGian
from app.models.SanBay import Sanbay
from app.models.HangVe import HangVe
from app import db
from .QuyDinh_service import get_quydinh_service
from .ChiTietHangve_service import add_ChiTietHangVe_service
from app.utils.validators import valadate_ChuyenBay, Validate_ChiTietChuyenBay, validate_timeRange, validate_NgayGio, format_NgayGio
from library import *
from sqlalchemy import extract, func
from app.utils.auth import is_admin


'''
    {
    "Ma_chuyen_bay": 6,
    "Ma_san_bay_di": "HNOI",
    "Ma_san_bay_den": "SGON",
    "gia_ve": 500000,
    "ngay_khoi_hanh": "2025-04-25",
    "gio_khoi_hanh": "00:00:00",
    "thoi_gian_bay": 30,
    "chitiet":[
        {
            "Ma_san_bay_trung_gian": "DNANG",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 1"
        },
        {
            "Ma_san_bay_trung_gian": "Vinh",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 2"
        }
    ],
    "hangve": [
        {
            "Ma_hang_ve": 1,
            "So_ghe_trong_hang": 50
        },
        {
            "Ma_hang_ve": 2,
            "So_ghe_trong_hang": 50
        }
    ]
}    


'''


def add_ChuyenBay_service(data):
    if not is_admin():
        raise ValueError("Bạn không có quyền thực hiện hành động này")
    rule = get_quydinh_service()
    valadate_ChuyenBay(data, rule)

    ma_chuyen_bay = data['Ma_chuyen_bay']
    ma_san_bay_di = data['Ma_san_bay_di']
    ma_san_bay_den = data['Ma_san_bay_den']
    gia_ve = data['gia_ve']
    ngay_khoi_hanh = data['ngay_khoi_hanh']
    gio_khoi_hanh = data['gio_khoi_hanh']
    thoi_gian_bay = data['thoi_gian_bay']
    hangve = data.get('hangve', [])
    chitiet_list = data.get('chitiet', [])

    cb = Chuyenbay.query.get(ma_chuyen_bay)
    if cb:
        raise ValueError("Mã chuyến bay đã tồn tại")

    

    chuyenbay = Chuyenbay( id = ma_chuyen_bay,
                            Ma_san_bay_di = ma_san_bay_di, 
                            Ma_san_bay_den = ma_san_bay_den,
                            ngay_khoi_hanh = ngay_khoi_hanh,
                            gio_khoi_hanh = gio_khoi_hanh,
                            Thoi_gian_bay = thoi_gian_bay,
                            gia_ve = gia_ve)
    
    try: 

        db.session.add(chuyenbay)
        # db.session.commit()

        # Validate danh sách hàng vé
        if not isinstance(hangve, list):
            raise ValueError("Danh sách hàng vé không hợp lệ")
        for hang in hangve:
            data = {}
            data['Ma_hang_ve'] = hang.get('Ma_hang_ve')
            data['Ma_chuyen_bay'] = ma_chuyen_bay
            data['So_ve_trong'] = hang.get('So_ghe_trong_hang')
            data['So_ve_da_dat'] = 0
            hv = HangVe.query.get(data['Ma_hang_ve'])
            data['Gia_ve'] = hv.Ti_le_don_gia * gia_ve
            add_ChiTietHangVe_service(data)

        
        if not isinstance(chitiet_list, list):
            raise ValueError("Thông tin chi tiết không hợp lệ")
        Validate_ChiTietChuyenBay(chitiet_list, rule, ma_san_bay_di, ma_san_bay_den)
        
        for chitiet in chitiet_list:
            ma_san_bay_trung_gian = chitiet.get('Ma_san_bay_trung_gian')
            thoigian_dung = chitiet.get('thoigian_dung')
            ghichu = chitiet.get('ghichu')
            if ma_san_bay_trung_gian and thoigian_dung and ghichu:
                chitiet = ChiTietSanBayTrungGian(Ma_chuyen_bay = ma_chuyen_bay, Ma_san_bay_trung_gian = ma_san_bay_trung_gian,
                                        Thoi_gian_dung = thoigian_dung, Ghi_chu = ghichu)
                db.session.add(chitiet)
                db.session.commit()
                print(chitiet)
        
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")


{
    "Ma_chuyen_bay": 6,
    "Ma_san_bay_di": 1,
    "Ma_san_bay_den": 2,
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




def get_chuyenbay_byID_service(id):
    """
    Hàm lấy thông tin chuyến bay từ cơ sở dữ liệu.
    :param id: ID chuyến bay
    :return: Chuyến bay hoặc raise ValueError nếu không tìm thấy
    """
    chuyenbay = Chuyenbay.query.get(id)
    if not chuyenbay:
        raise ValueError("Không tìm thấy chuyến bay")
    
    res = chuyenbay.serialize()
    chitiet_hangve = chuyenbay.chi_tiet_hang_ve
    chitiet_sanbay_trung_gian = chuyenbay.chi_tiet_san_bay_trung_gian
    # Serialize từng phần tử trong collection
    res['chitiet_hangve'] = [hv.serialize() for hv in chitiet_hangve]
    res['chitiet_sanbay_trung_gian'] = [sb.serialize() for sb in chitiet_sanbay_trung_gian]
    return res



def get_sogheconlai(chuyenbay: Chuyenbay, hangve: int):
    if hangve == 1:
        return chuyenbay.so_ghe_hang1
    else:
        return chuyenbay.so_ghe_hang2
    
    
def set_sogheconlai(chuyenbay: Chuyenbay, hangve: int):
    if hangve == 1:
        chuyenbay.so_ghe_hang1 -= 1
    else:
        chuyenbay.so_ghe_hang2 -= 1
        


def get_dsChuyenBay_follow_time_service(start_time, end_time, sanbay_di, sanbay_den):
    """
    Lấy danh sách chuyến bay trong khoảng thời gian
    
    Args:
        start_time: Thời gian bắt đầu
        end_time: Thời gian kết thúc
        sanbay_di: Mã sân bay đi
        sanbay_den: Mã sân bay đến
        
    Returns:
        List[dict]: Danh sách các chuyến bay và thông tin liên quan
    """
    start_time, end_time = validate_timeRange(start_time, end_time)
    try:
        result = Chuyenbay.query.filter(
            Chuyenbay.Ma_san_bay_di == sanbay_di,
            Chuyenbay.Ma_san_bay_den == sanbay_den,
            Chuyenbay.ngay_khoi_hanh >= start_time,
            Chuyenbay.ngay_khoi_hanh <= end_time
        ).all()
        
        res = []
        for chuyenbay in result:
            temp = chuyenbay.serialize()
            chitiet_hangve = chuyenbay.chi_tiet_hang_ve
            chitiet_sanbay_trung_gian = chuyenbay.chi_tiet_san_bay_trung_gian
            # Serialize từng phần tử trong collection
            temp['chitiet_hangve'] = [hv.serialize() for hv in chitiet_hangve]
            temp['chitiet_sanbay_trung_gian'] = [sb.serialize() for sb in chitiet_sanbay_trung_gian]
            res.append(temp)

      
        return res
    except Exception as e:
        raise ValueError(f"Lỗi khi lấy danh sách chuyến bay: {str(e)}")



        '''

        result = Chuyenbay.query.filter(
            Chuyenbay.Ma_san_bay_di == 'HAIPHONG',
            Chuyenbay.Ma_san_bay_den == 'SGON',
            Chuyenbay.ngay_khoi_hanh >= '2025-04-20T00:00:00',
            Chuyenbay.ngay_khoi_hanh <= '2026-04-25T23:59:59',
            Chuyenbay.id == 18
        ).all()

    
        result = db.session.query(
            Chuyenbay,
            ChiTietHangVe,
            ChiTietSanBayTrungGian
        ).outerjoin(
            ChiTietHangVe,
            ChiTietHangVe.Ma_chuyen_bay == Chuyenbay.id
        ).outerjoin(
            ChiTietSanBayTrungGian,
            ChiTietSanBayTrungGian.Ma_chuyen_bay == Chuyenbay.id
        ).filter(
            Chuyenbay.Ma_san_bay_di == 'HAIPHONG',
            Chuyenbay.Ma_san_bay_den == 'SGON',
            Chuyenbay.ngay_khoi_hanh >= '2025-04-20T00:00:00',
            Chuyenbay.ngay_khoi_hanh <= '2026-04-25T23:59:59',
            Chuyenbay.id == 18
        ).all()
        for row in result:
            print(row)
        '''

    #     # Tạo dictionary để lưu trữ thông tin các chuyến bay
    #     flights_dict = {}
        
    #     for row in result:
    #         chuyenbay = row[0]
    #         chitiet_hangve = row[1]
    #         chitiet_sanbay = row[2]
            
    #         # Nếu chuyến bay chưa có trong dictionary
    #         if chuyenbay.id not in flights_dict:
    #             chuyenbay_dict = chuyenbay.__dict__
    #             # Thêm thông tin thời gian bay
    #             chuyenbay_dict['Thoi_gian_bay'] = chuyenbay.Thoi_gian_bay
    #             flights_dict[chuyenbay.id] = {
    #                 'chuyenbay': chuyenbay_dict,
    #                 'chitiet_hangve': [],
    #                 'chitiet_sanbay_trunggian': []
    #             }
            
    #         # Thêm thông tin hàng vé nếu có
    #         if chitiet_hangve:
    #             # Kiểm tra xem hàng vé đã tồn tại trong danh sách chưa
    #             if not any(hv['Ma_hang_ve'] == chitiet_hangve.Ma_hang_ve 
    #                       for hv in flights_dict[chuyenbay.id]['chitiet_hangve']):
    #                 flights_dict[chuyenbay.id]['chitiet_hangve'].append(chitiet_hangve.__dict__)
            
    #         # Thêm thông tin sân bay trung gian nếu có
    #         if chitiet_sanbay:
    #             # Kiểm tra xem sân bay trung gian đã tồn tại trong danh sách chưa
    #             if not any(sb['Ma_san_bay_trung_gian'] == chitiet_sanbay.Ma_san_bay_trung_gian 
    #                       for sb in flights_dict[chuyenbay.id]['chitiet_sanbay_trunggian']):
    #                 flights_dict[chuyenbay.id]['chitiet_sanbay_trunggian'].append(chitiet_sanbay.__dict__)
        

    #     for flight in flights_dict.values():
    #         print(flight)
    #     # Chuyển đổi dictionary thành list
    #     flights_list = list(flights_dict.values())
        
    #     if not flights_list:
    #         raise ValueError("Không tìm thấy chuyến bay nào thỏa mãn điều kiện")
            
    #     return flights_list
        
    # except Exception as e:
    #     raise ValueError(f"Lỗi khi lấy danh sách chuyến bay: {str(e)}")

    




def update_chuyenbay_thoigianbay_service(chuyenbay_id, thoigianbay: int):
    try:
        chuyenbay = Chuyenbay.query.get(chuyenbay_id)
        if not chuyenbay:
            raise ValueError("Không tìm thấy chuyến bay")
        # validate_NgayGio(thoigianbay)
        # thoigianbay = format_NgayGio(thoigianbay)
        chuyenbay.Thoi_gian_bay = thoigianbay
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi không xác định: {e}")
    

def update_chuyenbay_ngaygiobay_service(chuyenbay_id, ngaygiobay):
    try:
        chuyenbay = Chuyenbay.query.get(chuyenbay_id)
        if not chuyenbay:
            raise ValueError("Không tìm thấy chuyến bay")
        validate_NgayGio(ngaygiobay)
        # thoigianbay = format_NgayGio(thoigianbay)
        chuyenbay.ngay_gio = ngaygiobay
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi không xác định: {e}")


def get_Chuyenbay_by_thang_service(thang, nam):
    ds = Chuyenbay.query.filter(
        extract('month', Chuyenbay.ngay_khoi_hanh) == thang,
        extract('year', Chuyenbay.ngay_khoi_hanh) == nam
    ).all()
    return ds



def update_chuyenbay_service(id, data):
    try:
        chuyenbay = Chuyenbay.query.get(id)
        if not chuyenbay:
            raise ValueError("Không tìm thấy chuyến bay")
        
        # Validate dữ liệu đầu vào
        if 'ngay_khoi_hanh' in data:
            chuyenbay.ngay_khoi_hanh = data['ngay_khoi_hanh']
        if 'gio_khoi_hanh' in data:
            chuyenbay.gio_khoi_hanh = data['gio_khoi_hanh']
        if 'Thoi_gian_bay' in data:
            chuyenbay.Thoi_gian_bay = data['Thoi_gian_bay']

        if 'gia_ve' in data:
            chuyenbay.gia_ve = data['gia_ve']
            db.session.query(ChiTietHangVe).filter(
                ChiTietHangVe.Ma_chuyen_bay == chuyenbay.id
            ).update({
                ChiTietHangVe.Gia_ve: data['gia_ve']*float(db.session.query(HangVe).filter(
                    HangVe.id == ChiTietHangVe.Ma_hang_ve
                ).first().Ti_le_don_gia)
            })
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi không xác định: {e}")
    

def Tong_soghedat_of_chuyenbay_service(chuyenbay: Chuyenbay):
    try:
        
        # Tính tổng số ghế đã đặt
        total_so_ve_da_dat = db.session.query(func.sum(ChiTietHangVe.So_ve_da_dat)).filter(
            ChiTietHangVe.Ma_chuyen_bay == chuyenbay.id
        ).scalar()
        
        return total_so_ve_da_dat or 0
    except Exception as e:
        raise ValueError(f"Lỗi khi tính tổng số ghế đã đặt: {str(e)}")
    

def Tong_soghetrong_of_chuyenbay_service(chuyenbay: Chuyenbay):
    try:
        
        # Tính tổng số ghế đã đặt
        total_so_ve_trong = db.session.query(func.sum(ChiTietHangVe.So_ve_trong)).filter(
            ChiTietHangVe.Ma_chuyen_bay == chuyenbay.id
        ).scalar()
        
        return total_so_ve_trong or 0
    except Exception as e:
        raise ValueError(f"Lỗi khi tính tổng số ghế trống: {str(e)}")