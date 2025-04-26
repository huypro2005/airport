from app.models.Chuyenbay import Chuyenbay
from app.models.ChiTietSanBayTrungGian import ChiTietSanBayTrungGian
from app.models.SanBay import Sanbay
from app.models.HangVe import HangVe
from app import db
from .QuyDinh_service import get_quydinh_service
from .ChiTietHangve_service import add_ChiTietHangVe_service
from app.utils.validators import valadate_ChuyenBay, Validate_ChiTietChuyenBay, validate_timeRange, validate_NgayGio, format_NgayGio
from library import *
from sqlalchemy import extract
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

        chitiet_list = data.get('chitiet', [])
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
                #
        
        
        db.session.commit()



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
    return chuyenbay



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
        


def get_dsChuyenBay_follow_time_service(start_time, end_time):
    """
    Lấy danh sách chuyến bay trong khoảng thời gian
    
    Args:
        start_time: Thời gian bắt đầu
        end_time: Thời gian kết thúc
        
    Returns:
        List[Chuyenbay]: Danh sách các chuyến bay thỏa điều kiện
    """
    start_time, end_time = validate_timeRange(start_time, end_time)
    return Chuyenbay.query.filter(
        Chuyenbay.ngay_khoi_hanh >= start_time,
        Chuyenbay.ngay_khoi_hanh <= end_time
    ).all()



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


def get_Chuyenbay_by_thang(thang, nam):
    ds = Chuyenbay.query.filter(
        extract('month', Chuyenbay.ngay_gio) == thang,
        extract('year', Chuyenbay.ngay_gio) == nam
    ).all()
    return ds

def clear_Chuyenbay_service(chuyenbay: Chuyenbay):
    '''
        Hàm cập nhật các phiếu đặt chỗ đã clear
    '''
    try:
        chuyenbay.clear = 1
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi chưa clear chuyến bay {chuyenbay.id}")


def check_Chuyenbay_is_flight(chuyenbay: Chuyenbay):
    '''
    Hàm kiểm tra chuyến bay có phải là chuyến bay bay hay không
    Nếu chuyến bay đã bay thì hủy tất cả phiếu đặt chỗ của chuyến bay đó
    '''

    from .PhieuDatCho_service import Huy_phieudatcho_through_chuyenbay_service
    Huy_phieudatcho_through_chuyenbay_service(chuyenbay)
    clear_Chuyenbay_service(chuyenbay)


def Huy_Phieudatcho_of_Chuyenbay_da_bay_service():
    try:
        ds = Chuyenbay.query.filter(
            Chuyenbay.ngay_gio < datetime.now(),
            Chuyenbay.clear == 0
        ).all()
        for chuyenbay in ds:
            check_Chuyenbay_is_flight(chuyenbay)
    except Exception as e:
        raise ValueError(f"Lỗi không xác định: {e}")

