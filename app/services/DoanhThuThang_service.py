from library import *
from app.models.DoanhThuThang import doanhThuThang
from app.models.Chuyenbay import Chuyenbay
from app.models.VeChuyenBay import Vechuyenbay
from app.models.ChiTietDoanhThuThang import ChiTietDoanhThuThang
from .ChiTietDoanhThuThang_service import update_tile_Chitietdoanhthu_service, create_or_update_chitietdoanhthuThang_service_bymonth
from sqlalchemy import func, case


def check_doanhthu_thang_service(thang, nam):

    try:
        doanhthuthang = doanhThuThang.query.filter(
            doanhThuThang.month == thang,
            doanhThuThang.year == nam
        ).first()
        if doanhthuthang is not None:
            return True
        else:
            return False
    except Exception as e:
        raise ValueError(f"Lỗi kiểm tra doanh thu tháng: {e}")



def create_or_update_doanhthu_thang_service(thang, nam):
    # if check_doanhthu_thang_service(thang, nam) == True:
    #     raise ValueError("Doanh thu tháng đã tồn tại")

    # find doanhthuthang if exist update, else create
    try:
        doanhthuthang = doanhThuThang.query.filter(
            doanhThuThang.month == thang,
            doanhThuThang.year == nam
        ).first()
    
        if doanhthuthang:
            doanhthuthang.Tong_doanh_thu, doanhthuthang.so_chuyen_bay = db.session.query(
                func.sum(ChiTietDoanhThuThang.Doanh_thu), func.sum(ChiTietDoanhThuThang.So_ghe_dat)
            ).filter(
                ChiTietDoanhThuThang.thang == thang,
                ChiTietDoanhThuThang.nam == nam
            ).first()
            if doanhthuthang.Tong_doanh_thu is None:
                doanhthuthang.Tong_doanh_thu = 0
            if doanhthuthang.so_chuyen_bay is None:
                doanhthuthang.so_chuyen_bay = 0

            try:
                update_tile_Chitietdoanhthu_service(thang, nam, doanhthuthang.Tong_doanh_thu, doanhthuthang.id)
            except Exception as e:
                db.session.rollback()
                raise ValueError(f"Lỗi cập nhật tỷ lệ chi tiết doanh thu tháng: {e}")

        else:
            doanhthuthang = doanhThuThang()
            doanhthuthang.month = thang
            doanhthuthang.year = nam
            doanhthuthang.so_chuyen_bay, doanhthuthang.Tong_doanh_thu = db.session.query(
                func.sum(ChiTietDoanhThuThang.So_ghe_dat), func.sum(ChiTietDoanhThuThang.Doanh_thu)
            ).filter(
                ChiTietDoanhThuThang.thang == thang,
                ChiTietDoanhThuThang.nam == nam
            ).first()
            if doanhthuthang.so_chuyen_bay is None:
                doanhthuthang.so_chuyen_bay = 0
            if doanhthuthang.Tong_doanh_thu is None:
                doanhthuthang.Tong_doanh_thu = 0
            doanhthuthang.Tile = 0
            db.session.add(doanhthuthang)
            db.session.commit()
            try:
                update_tile_Chitietdoanhthu_service(thang, nam, doanhthuthang.Tong_doanh_thu, doanhthuthang.id)
            except Exception as e:
                db.session.rollback()
                raise ValueError(f"Lỗi cập nhật tỷ lệ chi tiết doanh thu tháng: {e}")

        
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi tạo doanh thu tháng: {e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi tạo doanh thu tháng: {e}")

    
    

def update_tile_doanhthu_thang_service(nam, Tongdoanhthunam):
    try:
        db.session.query(doanhThuThang).filter(
            doanhThuThang.year == nam
        ).update({
            doanhThuThang.Tile: func.round(
                case(
                    (Tongdoanhthunam != 0, doanhThuThang.Tong_doanh_thu / Tongdoanhthunam),
                    else_=0
                ), 2
            )
        })
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi cập nhật tỷ lệ doanh thu tháng: {e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi cập nhật tỷ lệ doanh thu tháng: {e}")
    

def get_doanhthuthang_byid_service(id):
    try:
        doanhthuthang = doanhThuThang.query.filter(
            doanhThuThang.id == id
        ).first()
        if doanhthuthang is None:
            raise ValueError("Doanh thu tháng không tồn tại")
        return doanhthuthang
    except ValueError as e:
        raise ValueError(f"Lỗi lấy doanh thu tháng: {e}")
    except Exception as e:
        raise ValueError(f"Lỗi lấy doanh thu tháng: {e}")
    
def get_ds_doanhthuthang_service(nam):
    try:
        ds_doanhthuthang = db.session.query(doanhThuThang).filter(
            doanhThuThang.year == nam
        ).order_by(doanhThuThang.month).all()
        return ds_doanhthuthang
    except ValueError as e:
        raise ValueError(f"Lỗi lấy doanh thu tháng: {e}")
    except Exception as e:
        raise ValueError(f"Lỗi lấy doanh thu tháng: {e}")