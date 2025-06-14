from sqlalchemy import func, extract, case
from app.models.ChiTietDoanhThuThang import ChiTietDoanhThuThang
from app.models.DoanhThuThang import doanhThuThang
from app.models.Chuyenbay import Chuyenbay
from app.models.VeChuyenBay import Vechuyenbay
from .Chuyenbay_service import get_Chuyenbay_by_thang_service, Tong_soghedat_of_chuyenbay_service, Tong_soghetrong_of_chuyenbay_service
from library import *



def update_tile_Chitietdoanhthu_service(thang, nam, Tongdoanhthuthang, Ma_BCDTT):
    try:
        db.session.query(ChiTietDoanhThuThang).filter(
            ChiTietDoanhThuThang.thang == thang,
            ChiTietDoanhThuThang.nam == nam
        ).update({
            # round 2 decimal
            ChiTietDoanhThuThang.Ti_le: func.round(
                case(
                    (Tongdoanhthuthang != 0, ChiTietDoanhThuThang.Doanh_thu / Tongdoanhthuthang),
                    else_=0
                ), 2
            ),
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


# # Tạo hoặc cập nhật chi tiết doanh thu tháng cho từng vé chuyến bay

def create_or_update_chitietdoanhthuThang_service(vecb: Vechuyenbay):
    try:
        chitietdoanhthu = ChiTietDoanhThuThang.query.filter(
            ChiTietDoanhThuThang.Ma_chuyen_bay == vecb.Ma_chuyen_bay,
            ChiTietDoanhThuThang.thang == extract('month', vecb.Ngay_dat_ve) ,
            ChiTietDoanhThuThang.nam == extract('year', vecb.Ngay_dat_ve)
        ).first()

        if chitietdoanhthu:
            chitietdoanhthu.So_ghe_dat += 1
            chitietdoanhthu.Doanh_thu += vecb.Tien_ve
            db.session.commit()
        else:
            chitietdoanhthu = ChiTietDoanhThuThang()
            chitietdoanhthu.Ma_chuyen_bay = vecb.Ma_chuyen_bay
            chitietdoanhthu.thang = extract('month', vecb.Ngay_dat_ve)
            chitietdoanhthu.nam = extract('year', vecb.Ngay_dat_ve)
            chitietdoanhthu.So_ghe_dat = 1
            chitietdoanhthu.Doanh_thu = vecb.Tien_ve
            chitietdoanhthu.Ma_BCDTT = None
            chitietdoanhthu.Ti_le = 0
            db.session.add(chitietdoanhthu)
            db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi tạo hoặc cập nhật chi tiết doanh thu tháng: {e}")
    except Exception as e:
        raise ValueError(f"Lỗi tạo hoặc cập nhật chi tiết doanh thu tháng: {e}")
            
        
                
def create_or_update_chitietdoanhthuThang_service_bymonth(month, year):
    try:
        ds_vechuyenbay = Vechuyenbay.query.filter(
            extract('month', Vechuyenbay.Ngay_dat_ve) == month,
            extract('year', Vechuyenbay.Ngay_dat_ve) == year
        ).all()

        db.session.query(ChiTietDoanhThuThang).filter(
            ChiTietDoanhThuThang.thang == month,
            ChiTietDoanhThuThang.nam == year
        ).update({
            ChiTietDoanhThuThang.So_ghe_dat: 0,
            ChiTietDoanhThuThang.Doanh_thu: 0,
            ChiTietDoanhThuThang.Ti_le: 0,
            ChiTietDoanhThuThang.Ma_BCDTT: None
        })

        for vechuyenbay in ds_vechuyenbay:
            create_or_update_chitietdoanhthuThang_service(vechuyenbay)

        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi tạo hoặc cập nhật chi tiết doanh thu tháng: {e}")
    except Exception as e:
        raise ValueError(f"Lỗi tạo hoặc cập nhật chi tiết doanh thu tháng: {e}")
