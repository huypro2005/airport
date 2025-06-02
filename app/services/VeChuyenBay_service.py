from app.models.VeChuyenBay import Vechuyenbay
from app.models.Chuyenbay import Chuyenbay
from app.models.HanhKhach import HanhKhach
from app.models.ChiTietHangVe import ChiTietHangVe

from .QuyDinh_service import get_quydinh_service
from .Chuyenbay_service import get_sogheconlai, set_sogheconlai
from .HanhKhach_service import add_or_get_HanhKhach_service
from app.utils.validators import validate_VeChuyenBay,  validate_VeChuyenBay_seat
from .ChiTietHangve_service import get_ChiTietHangVe_service
from library import *



'''

    {
        "Ma_chuyen_bay": 1,
        "Ma_hang_ve": 1,
        "vitri": "B4.1",
        "Ho_ten": "nguyen van a",
        "cmnd": "116468466314",
        "sdt": "24544346",
        "gioi_tinh": "Nam"
    }

'''


def add_veChuyenyBay_service(data):
    rule = get_quydinh_service()
    if not rule:
        raise ValueError("Lỗi truy cập quy định.")
    try:
        validate_VeChuyenBay(data, rule)
        macb = data['Ma_chuyen_bay']
        Hoten = data['Ho_ten']
        cmnd = data['cmnd']
        sdt = data['sdt']
        gioi_tinh = data['gioi_tinh']
        ma_hang_ve = data['Ma_hang_ve']
        vi_tri = data['vitri']
        

        chuyenbay = Chuyenbay.query.get(macb)
        if not chuyenbay:
            raise ValueError("Chuyến bay không tồn tại")
        chiTietHangVe = get_ChiTietHangVe_service(macb, ma_hang_ve)
        if chiTietHangVe is None:
            raise ValueError("Hạng vé không tồn tại")
        

        # kiem tra thoi gian dat ve phai nho hon thoi gian khoi hanh, va toi thieu la truoc 24h
        if datetime.now().date() > chuyenbay.ngay_khoi_hanh:
            raise ValueError('Chuyến bay đã khởi hành')

        if chuyenbay.ngay_khoi_hanh - datetime.now().date() < timedelta(days=rule.ThoiGianDatVeToiThieu):
            raise ValueError("Thời gian đặt vé phải trước 24h so với giờ khởi hành")

        ngay_dat = datetime.now().date()
        

        validate_VeChuyenBay_seat(vi_tri, macb)
        data = {
            'Hoten': Hoten,
            'cmnd': cmnd,
            'sdt': sdt,
            'gioi_tinh': gioi_tinh
        }
        hanhkhach = add_or_get_HanhKhach_service(data)
        vechuyenbay = Vechuyenbay()
        vechuyenbay.Ma_chuyen_bay = macb
        vechuyenbay.Ma_hang_ve = ma_hang_ve
        vechuyenbay.vi_tri = vi_tri
        vechuyenbay.Ma_hanh_khach = hanhkhach.id
        vechuyenbay.Tien_ve = chiTietHangVe.Gia_ve
        vechuyenbay.Ngay_dat_ve = ngay_dat

        chiTietHangVe.So_ve_da_dat += 1
        chiTietHangVe.So_ve_trong -= 1  

        db.session.add(vechuyenbay)
        db.session.commit()
        return vechuyenbay
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi: {e}")
        
        



{
    "Ma_chuyen_bay": 1,
    "Ho_ten" : "Dau Thi Vy",
    "cmnd": "234556456",
    "sdt": "546362",
    "gioi_tinh": "Nu",
    "hang_ve": 1,
    "vitri": "B5.1"
}   




def get_veChuyenBay_byID_service(id):
    ve_chuyen_bay = Vechuyenbay.query.get(id)
    if ve_chuyen_bay:
        return ve_chuyen_bay
    else:
        return None




def delete_ve_service(id):
    ve = Vechuyenbay.query.get(id)
    if ve:
        db.session.delete(ve)
        db.session.commit()
    else:
        raise ValueError("Không tìm thấy vé")

# def giave_chuyenbay_follow_hangve_service(chuyenbay: Chuyenbay, hangve: int):
#     rule = get_quydinh_service()
#     if not rule:
#         raise ValueError("Lỗi truy cập quy định.")
#     if hangve == 1:
#         return chuyenbay.gia_ve * rule.Phantramgia1/100
#     else:
#         return chuyenbay.gia_ve * rule.Phantramgia2/100




def get_ds_veChuyenBay_by_HanhKhach_service(hk_cmnd):
    # ds_ve = Vechuyenbay.query.filter(
    #     Vechuyenbay.Ma_hanh_khach == hk_id # Chỉ lấy vé đã đặt
    #     and Vechuyenbay.Ma_hang_ve != None # Chỉ lấy vé có hạng vé
    # ).all()

    ds_ve = db.session.query(Vechuyenbay).join(HanhKhach).filter(
        HanhKhach.cmnd == hk_cmnd,
        Vechuyenbay.Ma_hang_ve != None  # Chỉ lấy vé có hạng vé
    ).all()


    if ds_ve:
        return ds_ve
    else:
        return None