from .ChiTietChuyenBay import ChiTietChuyenBay
from .Chuyenbay import Chuyenbay
from .HanhKhach import HanhKhach
from .Maybay import Maybay
from .PhieuDatCho import PhieuDatCho
from .SanBay import Sanbay
from .VeChuyenBay import Vechuyenbay
from .DoanhThuNam import doanhThuNam
from .DoanhThuThang import doanhThuThang
from .HoaDon import Hoadon
from .NhanVien import Nhanvien
from .QuyDinh import QuyDinh
from app import db


def create_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # Create all tables in the database
        print("Database tables created successfully.")
