from app.models import Chuyenbay, ChiTietChuyenBay, Sanbay, Maybay, QuyDinh
from app import db
from .QuyDinh_service import get_quydinh
from app.utils.validators import valadate_ChuyenBay, Validate_ChiTietChuyenBay, validate_timeRange, validate_NgayGio
from library import *

def add_ChuyenBay_service(data):
    '''
    
    
    '''
    rule = get_quydinh()
    valadate_ChuyenBay(data, rule)

    ma_chuyen_bay = data['Ma_chuyen_bay']
    ma_san_bay_di = data['Ma_san_bay_di']
    ma_san_bay_den = data['Ma_san_bay_den']
    ma_may_bay = data['Ma_may_bay']
    gia_ve = data['gia_ve']
    ngay_gio_str = data['ngay_gio']
    thoi_gian_bay = data['thoi_gian_bay']
    so_ghe_hang1 = data['so_ghe_hang1']
    so_ghe_hang2 = data['so_ghe_hang2']
    tongsoghe = so_ghe_hang1 + so_ghe_hang2
    

    cb = Chuyenbay.query.get(ma_chuyen_bay)
    if cb:
        raise ValueError("Mã chuyến bay đã tồn tại")

    try:
        # Dùng datetime.strptime để chuyển đổi chuỗi thành datetime object
        ngay_gio = datetime.strptime(ngay_gio_str, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        raise ValueError("Ngày giờ không hợp lệ. Định dạng phải là YYYY-MM-DDTHH:MM:SS")

    chuyenbay = Chuyenbay( id = ma_chuyen_bay,
                            Ma_san_bay_di = ma_san_bay_di, 
                            Ma_san_bay_den = ma_san_bay_den,
                            Ma_may_bay = ma_may_bay,
                            ngay_gio = ngay_gio,
                            Thoi_gian_bay = thoi_gian_bay,
                            gia_ve = gia_ve,
                            so_ghe_hang1 = so_ghe_hang1,
                            so_ghe_hang2 = so_ghe_hang2,
                            tong_so_ghe = tongsoghe )
    
    try: 

        db.session.add(chuyenbay)
        # db.session.commit()
        chitiet_list = data.get('chitiet', [])
        if not isinstance(chitiet_list, list):
            raise ValueError("Thông tin chi tiết không hợp lệ")
        Validate_ChiTietChuyenBay(chitiet_list, rule, ma_san_bay_di, ma_san_bay_den)
        
        for chitiet in chitiet_list:
            ma_san_bay_trung_gian = chitiet.get('Ma_san_bay_trung_gian')
            thoigian_dung = chitiet.get('thoigian_dung')
            ghichu = chitiet.get('ghichu')
            if ma_san_bay_trung_gian and thoigian_dung and ghichu:
                chitiet = ChiTietChuyenBay(Ma_chuyen_bay = ma_chuyen_bay, Ma_san_bay_trung_gian = ma_san_bay_trung_gian,
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
        Chuyenbay.ngay_gio >= start_time,
        Chuyenbay.ngay_gio <= end_time
    ).all()


def clear_Chuyenbay_service(chuyenbay: Chuyenbay):
    chuyenbay.clear = 1
    db.session.commit()


def check_Chuyenbay_is_flight(chuyenbay: Chuyenbay):
    if chuyenbay.ngay_gio < datetime.now() and chuyenbay.clear == 0:
        from .PhieuDatCho_service import Huy_phieudatcho_through_chuyenbay_service
        Huy_phieudatcho_through_chuyenbay_service(chuyenbay)
        clear_Chuyenbay_service(chuyenbay)



def update_chuyenbay_thoigianbay_service(chuyenbay_id, thoigianbay: int):
    try:
        chuyenbay = Chuyenbay.query.get(chuyenbay_id)
        if not chuyenbay:
            raise ValueError("Không tìm thấy chuyến bay")
        validate_NgayGio(thoigianbay)
        chuyenbay.thoigianbay = thoigianbay
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi không xác định: {e}")



def get_Chuyenbay_by_thang(thang):
    ds = Chuyenbay.query.filter(
        Chuyenbay.ngay_gio.month == thang
    ).all()
    return ds




