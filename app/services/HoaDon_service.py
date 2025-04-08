from app.models.HoaDon import Hoadon
from app.models.VeChuyenBay import Vechuyenbay
from app.utils.validators import validate_Hoadon
from flask import session
from library import *

def create_hoadon_through_vechuyenbay_service(vechuyenbay: Vechuyenbay, hoadon: Hoadon):  
    hoadon.Ma_hanh_khach = vechuyenbay.Ma_hanh_khach
    hoadon.Ma_nhan_vien = 1
    hoadon.Loai_hoa_don = 0
    hoadon.Ma_ve_cb = vechuyenbay.id
    hoadon.Thanh_tien = vechuyenbay.Tien_ve


def create_hoadon_service(data, nhanvien_id):
    validate_Hoadon(data)
    ma_hanh_khach = data['Ma_hanh_khach']
    ma_ve_cb = data['Ma_ve_cb']
    loai_hoa_don = 0
    thanh_tien = data['Thanh_tien']
    ghi_chu = data['Ghi_chu']

    hoadon = Hoadon(Ma_hanh_khach = ma_hanh_khach, Ma_ve_cb = ma_ve_cb, Ma_nhan_vien = nhanvien_id, Loai_hoa_don = loai_hoa_don, Thanh_tien = thanh_tien, Ghi_chu = ghi_chu)
    try:
        db.session.add(hoadon)
        db.session.commit()
        return hoadon
    except:
        raise ValueError("Lỗi thêm hóa đơn")
    
def create_Hoadon_hoantien_service(vechuyenbay: Vechuyenbay, hoadon: Hoadon):
    hoadon.Ma_hanh_khach = vechuyenbay.Ma_hanh_khach
    hoadon.Ma_nhan_vien = 1
    hoadon.Loai_hoa_don = 1
    hoadon.Ma_ve_cb = vechuyenbay.id



def create_Hoadon_themtien_service(vechuyenbay: Vechuyenbay, hoadon: Hoadon):
    hoadon.Ma_hanh_khach = vechuyenbay.Ma_hanh_khach
    hoadon.Ma_nhan_vien = 1
    hoadon.Loai_hoa_don = 0
    hoadon.Ma_ve_cb = vechuyenbay.id
