from .Chuyenbay import Chuyenbay
from .HanhKhach import HanhKhach
from .SanBay import Sanbay
from .VeChuyenBay import Vechuyenbay
from .DoanhThuThang import doanhThuThang
from .HangVe import HangVe
from .NhanVien import Nhanvien
from .QuyDinh import QuyDinh
from .ChiTietDoanhThuThang import ChiTietDoanhThuThang
from .ChiTietHangVe import ChiTietHangVe
from .ChiTietSanBayTrungGian import ChiTietSanBayTrungGian
from .DoangThuNam import DoanhThuNam
from app import db


def create_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # Create all tables in the database
        print("Database tables created successfully.")
