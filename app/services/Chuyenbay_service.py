from app.models.ChiTietHangVe import ChiTietHangVe
from app.models.Chuyenbay import Chuyenbay
from app.models.ChiTietSanBayTrungGian import ChiTietSanBayTrungGian
from app.models.SanBay import Sanbay
from app.models.HangVe import HangVe
from app import db
from .QuyDinh_service import get_quydinh_service
from .ChiTietHangve_service import add_ChiTietHangVe_service
from .SanBay_service import check_SanBay_Active
from .HangVe_service import check_hangve_active
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
    check_duplicate_sbtg = set()

    for chitiet in chitiet_list:
        if  chitiet.get('Ma_san_bay_trung_gian') == ma_san_bay_den or chitiet.get('Ma_san_bay_trung_gian') == ma_san_bay_di:
            raise ValueError("Sân bay trung gian không được trùng với sân bay đi hoặc đến")
        if not check_SanBay_Active(chitiet.get('Ma_san_bay_trung_gian')):
            raise ValueError(f"Sân bay trung gian {chitiet.get('Ma_san_bay_trung_gian')} không tồn tại hoặc đã bị xóa")
        if chitiet.get('thoigian_dung') <= 0 or chitiet.get('thoigian_dung') > rule.Thoigiandungtoida:
            raise ValueError(f"Thời gian dừng phải lớn hơn {rule.Thoigiandungtoithieu} và nhỏ hơn hoặc bằng thời gian dừng tối đa quy định {rule.Thoigiandungtoida}")
        if chitiet.get('Ma_san_bay_trung_gian') in check_duplicate_sbtg:
            raise ValueError(f"Sân bay trung gian {chitiet.get('Ma_san_bay_trung_gian')} đã được thêm trước đó")
        check_duplicate_sbtg.add(chitiet.get('Ma_san_bay_trung_gian'))


    if len(chitiet_list) > rule.Soluongsanbaytrunggian:
        raise ValueError(f"Số lượng sân bay trung gian không được vượt quá {rule.Soluongsanbaytrunggian}")
    for hang in hangve:
        if not check_hangve_active(hang.get('Ma_hang_ve')):
            raise ValueError(f"Hạng vé {hang.get('Ma_hang_ve')} không tồn tại hoặc đã bị xóa")
    if not check_SanBay_Active(ma_san_bay_di):
        raise ValueError(f"Sân bay đi {ma_san_bay_di} không tồn tại hoặc đã bị xóa")
    if not check_SanBay_Active(ma_san_bay_den):
        raise ValueError(f"Sân bay đến {ma_san_bay_den} không tồn tại hoặc đã bị xóa")
    

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
    # lấy các chi tiết hạng vé mà hạng vé còn hoạt động
    chitiet_hangve = [hv for hv in chitiet_hangve if check_hangve_active(hv.Ma_hang_ve)]    
    chitiet_sanbay_trung_gian = chuyenbay.chi_tiet_san_bay_trung_gian
    # Serialize từng phần tử trong collection
    res['chitiet_hangve'] = [hv.serialize() for hv in chitiet_hangve]
    res['chitiet_sanbay_trung_gian'] = [sb.serialize() for sb in chitiet_sanbay_trung_gian]
    return res




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
            # # Serialize từng phần tử trong collection
            # temp['chitiet_hangve'] = [hv.serialize() for hv in chitiet_hangve if check_hangve_active(hv.Ma_hang_ve)]
            # # Lọc các sân bay trung gian còn hoạt động
            # temp['chitiet_sanbay_trung_gian'] = [sb.serialize() for sb in chitiet_sanbay_trung_gian]
            res.append(temp)

      
        return res
    except Exception as e:
        raise ValueError(f"Lỗi khi lấy danh sách chuyến bay: {str(e)}")






# def update_chuyenbay_thoigianbay_service(chuyenbay_id, thoigianbay: int):
#     try:
#         chuyenbay = Chuyenbay.query.get(chuyenbay_id)
#         if not chuyenbay:
#             raise ValueError("Không tìm thấy chuyến bay")
#         # validate_NgayGio(thoigianbay)
#         # thoigianbay = format_NgayGio(thoigianbay)
#         chuyenbay.Thoi_gian_bay = thoigianbay
#         db.session.commit()
#     except ValueError as e:
#         db.session.rollback()
#         raise ValueError(f"{e}")
#     except Exception as e:
#         db.session.rollback()
#         raise ValueError(f"Lỗi không xác định: {e}")
    

# def update_chuyenbay_ngaygiobay_service(chuyenbay_id, ngaygiobay):
#     try:
#         chuyenbay = Chuyenbay.query.get(chuyenbay_id)
#         if not chuyenbay:
#             raise ValueError("Không tìm thấy chuyến bay")
#         validate_NgayGio(ngaygiobay)
#         # thoigianbay = format_NgayGio(thoigianbay)
#         chuyenbay.ngay_gio = ngaygiobay
#         db.session.commit()
#     except ValueError as e:
#         db.session.rollback()
#         raise ValueError(f"{e}")
#     except Exception as e:
#         db.session.rollback()
#         raise ValueError(f"Lỗi không xác định: {e}")


def get_Chuyenbay_by_thang_service(thang, nam):
    ds = Chuyenbay.query.filter(
        extract('month', Chuyenbay.ngay_khoi_hanh) == thang,
        extract('year', Chuyenbay.ngay_khoi_hanh) == nam
    ).all()
    return ds


'''
{
    "ngay_khoi_hanh": "2025-04-25",
    "gio_khoi_hanh": "00:00:00",
    "gia_ve": 1000000,
    "Thoi_gian_bay": 40,
    "chitiet":[
        {
            "Ma_san_bay_trung_gian": "DNANG",
            "thoigian_dung": 15,
            "ghichu": "Tg 1",
            "is_delete": 0
        },
        {
            "Ma_san_bay_trung_gian": "Vinh",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 2",
            "is_delete": 1
        }
    ]
}
'''

def update_chuyenbay_service(id, data):
    try:
        chuyenbay = Chuyenbay.query.get(id)
        if not chuyenbay:
            raise ValueError("Không tìm thấy chuyến bay")
        
        if chuyenbay.ngay_khoi_hanh <= (datetime.now().date()):
            raise ValueError("Chuyến bay đã khởi hành, không thể cập nhật thông tin")

        # Validate dữ liệu đầu vào
        if 'ngay_khoi_hanh' in data:
            ngayKhoiHanh = datetime.strptime(data['ngay_khoi_hanh'], "%Y-%m-%d").date()
            if ngayKhoiHanh < (datetime.now().date() - timedelta(days=1)):
                raise ValueError("Ngày khởi hành không được nhỏ hơn ngày hiện tại")
            chuyenbay.ngay_khoi_hanh = ngayKhoiHanh
        if 'gio_khoi_hanh' in data:
            chuyenbay.gio_khoi_hanh = data['gio_khoi_hanh']
        if 'Thoi_gian_bay' in data:
            chuyenbay.Thoi_gian_bay = data['Thoi_gian_bay']
        ds_sbtrunggian = chuyenbay.chi_tiet_san_bay_trung_gian
        if 'chitiet' in data:
            ds_chitiet = data['chitiet']
            for chitiet in ds_chitiet:
                ct_trunggian = next((ct for ct in ds_sbtrunggian if ct.Ma_san_bay_trung_gian == chitiet['Ma_san_bay_trung_gian']), None)
                if ct_trunggian:
                    if chitiet['is_delete'] == 1:
                        db.session.delete(ct_trunggian)
                    else:
                        ct_trunggian.Thoi_gian_dung = chitiet['thoigian_dung']
                        ct_trunggian.Ghi_chu = chitiet['ghichu']
                else:
                    raise ValueError("Sân bay trung gian không tồn tại")

        if 'gia_ve' in data:
            chuyenbay.gia_ve = data['gia_ve']

            # db.session.query(ChiTietHangVe).filter(
            #     ChiTietHangVe.Ma_chuyen_bay == chuyenbay.id
            # ).update({
            #     ChiTietHangVe.Gia_ve: data['gia_ve']*float(db.session.query(HangVe).filter(
            #         HangVe.id == ChiTietHangVe.Ma_hang_ve
            #     ).first().Ti_le_don_gia)
            # })
            ctHangve = chuyenbay.chi_tiet_hang_ve
            for ct in ctHangve:
                ct.Gia_ve = data['gia_ve'] * float(db.session.query(HangVe).filter(
                    HangVe.id == ct.Ma_hang_ve
                ).first().Ti_le_don_gia)

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
    

def delete_chuyenbay_service(id):
    try:
        chuyenbay = Chuyenbay.query.get(id)
        if not chuyenbay:
            raise ValueError("Không tìm thấy chuyến bay")

        # Kiểm tra xem chuyến bay đã hoạt động hay chưa
        vecb = chuyenbay.ve_chuyen_bay
        if vecb:
            raise ValueError("Không thể xóa chuyến bay đã có vé đặt")
        # Xóa các chi tiết hạng vé liên quan
        ChiTietHangVe.query.filter(ChiTietHangVe.Ma_chuyen_bay == id).delete()
        
        # Xóa các chi tiết sân bay trung gian liên quan
        ChiTietSanBayTrungGian.query.filter(ChiTietSanBayTrungGian.Ma_chuyen_bay == id).delete()
        
        db.session.delete(chuyenbay)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")
    
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi không xác định: {e}")