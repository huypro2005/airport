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
import time


def create_db(app):
    try:
        with app.app_context():
            # Chỉ chạy nếu chưa có bảng nào
            print("Checking if database tables exist...")
            db.init_app(app)
            db.create_all()
            
            # Tạo dữ liệu mặc định nếu cần
            if not QuyDinh.query.first():
                db.session.add(QuyDinh())
                db.session.commit()
            
                print("Created new database tables")
            else:
                print("Database already initialized")
            
    except Exception as e:
        print(f"Database error: {e}")
        raise