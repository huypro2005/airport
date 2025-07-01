from app.models.DoangThuNam import DoanhThuNam
from app.models.DoanhThuThang import doanhThuThang
from app import db
from .DoanhThuThang_service import update_tile_doanhthu_thang_service, create_or_update_doanhthu_thang_service
from sqlalchemy import func
import asyncio

# Create or update doanh thu tháng for a specific month and year
def create_all_doanhthu_thang_service(year):
    try:
        for i in range(1, 13):
            create_or_update_doanhthu_thang_service(i, year)
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi tạo doanh thu tháng: {e}")



def create_or_update_doanhthu_nam_service(nam):
    try:
        doanhthunam = DoanhThuNam.query.filter(
            DoanhThuNam.year == nam
        ).first()
        if doanhthunam:
            doanhthunam.Tong_doanh_thu = db.session.query(
                func.sum(doanhThuThang.Tong_doanh_thu)
            ).filter(
                doanhThuThang.year == nam
            ).scalar()
            if doanhthunam.Tong_doanh_thu is None:
                doanhthunam.Tong_doanh_thu = 0
            
        else:   
            doanhthunam = DoanhThuNam()
            doanhthunam.year = nam
            doanhthunam.Tong_doanh_thu = db.session.query(
                func.sum(doanhThuThang.Tong_doanh_thu)
            ).filter(
                doanhThuThang.year == nam
            ).scalar()
            if doanhthunam.Tong_doanh_thu is None:
                doanhthunam.Tong_doanh_thu = 0
            db.session.add(doanhthunam)
        db.session.commit()
        
        update_tile_doanhthu_thang_service(nam, doanhthunam.Tong_doanh_thu)
    except ValueError as e: 
        db.session.rollback()
        raise ValueError(f"Lỗi tạo doanh thu năm: {e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi tạo doanh thu năm: {e}")
        

def update_doanhthu_nam_service(nam):
    try:
        doanhthunam = DoanhThuNam.query.filter(
            DoanhThuNam.year == nam
        ).first()
        if doanhthunam is None:
            raise ValueError("Doanh thu năm không tồn tại")
        doanhthunam.Tong_doanh_thu = db.session.query(
            func.sum(doanhThuThang.Tong_doanh_thu)
        ).filter(
            doanhThuThang.year == nam
        ).scalar()
        if doanhthunam.Tong_doanh_thu is None:
            doanhthunam.Tong_doanh_thu = 0
        db.session.commit()
        try:
            update_tile_doanhthu_thang_service(nam, doanhthunam.Tong_doanh_thu)
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Lỗi cập nhật tỷ lệ doanh thu tháng: {e}")
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"Lỗi cập nhật doanh thu năm: {e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi cập nhật doanh thu năm: {e}")