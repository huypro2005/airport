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
    max_retries = 5
    retry_delay = 5  # seconds
    for attempt in range(max_retries):
        try:
            db.init_app(app)
            with app.app_context():
                db.create_all()
                d = QuyDinh.query.first()
                if d is None:
                    quy_dinh = QuyDinh()
                    db.session.add(quy_dinh)
                    db.session.commit()
                else:
                    pass
                
                print("Database connection established and tables created successfully.")
            break  # If successful, exit the loop
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Exiting.")
                raise   