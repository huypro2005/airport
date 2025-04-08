from library import *
from app.models.DoanhThuThang import DoanhThuThang
from app.models.Chuyenbay import Chuyenbay
from app.models.VeChuyenBay import Vechuyenbay
from .Chuyenbay_service import get_Chuyenbay_by_thang



def get_doanh_thu_chuyenbay_by_thang_service(thang):
    ds = get_Chuyenbay_by_thang(thang)
    data =[]
    for chuyenbay in ds:
        item = {}
        item['ma_chuyen_bay'] = chuyenbay.id
        vechuyenbay = chuyenbay.ve_chuyen_bay
        for ve in vechuyenbay:
            if ve.Tinh_trang == False:
                item['doanh_thu'] += ve.Tien_ve
                item['so_ve_ban'] += 1
        data.append(item)
    return data
        
