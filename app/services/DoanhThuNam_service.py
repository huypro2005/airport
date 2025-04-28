from app.models.DoangThuNam import DoanhThuNam
from app.models.DoanhThuThang import doanhThuThang
from app import db
from .DoanhThuThang_service import update_tile_doanhthu_thang_service
from sqlalchemy import func



def create_doanhthu_nam_service(nam):
    if DoanhThuNam.query.filter(
        DoanhThuNam.year == nam
    ).first() is not None:
        raise ValueError("Doanh thu năm đã tồn tại")
    try:
        doanhthunam = DoanhThuNam()
        doanhthunam.year = nam
        doanhthunam.Tong_doanh_thu = db.session.query(
            func.sum(doanhThuThang.Tong_doanh_thu)
        ).filter(
            doanhThuThang.year == nam
        ).scalar()
        if doanhthunam.Tong_doanh_thu is None:
            doanhthunam.Tong_doanh_thu = 0
        update_tile_doanhthu_thang_service(nam, doanhthunam.Tong_doanh_thu)
        db.session.add(doanhthunam)
        db.session.commit()
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