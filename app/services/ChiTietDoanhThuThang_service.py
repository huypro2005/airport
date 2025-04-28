from math import e
from sqlalchemy import func
from app.models.ChiTietDoanhThuThang import ChiTietDoanhThuThang
from app.models.DoanhThuThang import doanhThuThang
from app.models.Chuyenbay import Chuyenbay
from app.models.VeChuyenBay import Vechuyenbay
from .Chuyenbay_service import get_Chuyenbay_by_thang_service, Tong_soghedat_of_chuyenbay_service, Tong_soghetrong_of_chuyenbay_service
from library import *


def create_ds_chitietdoanhthu_service(thang, nam):
    try:

        ds_chuyenbay = get_Chuyenbay_by_thang_service(thang, nam)
        for chuyenbay in ds_chuyenbay:
            if ChiTietDoanhThuThang.query.filter(
                ChiTietDoanhThuThang.Ma_chuyen_bay == chuyenbay.id,
                ChiTietDoanhThuThang.thang == thang,
                ChiTietDoanhThuThang.nam == nam
            ).first():
                continue
            chitietdoanhthu = ChiTietDoanhThuThang()
            chitietdoanhthu.Ma_chuyen_bay = chuyenbay.id
            chitietdoanhthu.thang = thang
            chitietdoanhthu.nam = nam   
            chitietdoanhthu.So_ghe_dat = Tong_soghedat_of_chuyenbay_service(chuyenbay)
            chitietdoanhthu.So_ghe_trong = Tong_soghetrong_of_chuyenbay_service(chuyenbay)
            chitietdoanhthu.Ti_le = 0
            chitietdoanhthu.Doanh_thu = db.session.query(func.sum(Vechuyenbay.Tien_ve)).filter(
                Vechuyenbay.Ma_chuyen_bay == chuyenbay.id,
                Vechuyenbay.Tinh_trang == True
            ).scalar()
            if chitietdoanhthu.Doanh_thu is None:
                chitietdoanhthu.Doanh_thu = 0   
            chitietdoanhthu.Ma_BCDTT = None
            db.session.add(chitietdoanhthu)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi tạo chi tiết doanh thu tháng: {e}")
    except Exception as e:
        raise ValueError(f"Lỗi tạo chi tiết doanh thu tháng: {e}")



def update_tile_Chitietdoanhthu_service(thang, nam, Tongdoanhthuthang, Ma_BCDTT):
    try:
        db.session.query(ChiTietDoanhThuThang).filter(
            ChiTietDoanhThuThang.thang == thang,
            ChiTietDoanhThuThang.nam == nam
        ).update({
            ChiTietDoanhThuThang.Ti_le: ChiTietDoanhThuThang.Doanh_thu / Tongdoanhthuthang if Tongdoanhthuthang != 0 else 0,
            ChiTietDoanhThuThang.Ma_BCDTT: Ma_BCDTT
        })
        
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi cập nhật tỷ lệ chi tiết doanh thu tháng: {e}")
    except Exception as e:
        raise ValueError(f"Lỗi cập nhật tỷ lệ chi tiết doanh thu tháng: {e}")
    



def get_ds_chitietdoanhthu_service(thang, nam):
    try:
        ds_chitietdoanhthu = db.session.query(ChiTietDoanhThuThang).filter(
            ChiTietDoanhThuThang.thang == thang,
            ChiTietDoanhThuThang.nam == nam
        ).all()
        if ds_chitietdoanhthu is None:
            raise ValueError("Không tìm thấy chi tiết doanh thu tháng")
        return ds_chitietdoanhthu
    except ValueError as e:
        raise ValueError(f"Lỗi lấy danh sách chi tiết doanh thu tháng: {e}")
    except Exception as e:
        raise ValueError(f"Lỗi lấy danh sách chi tiết doanh thu tháng: {e}")