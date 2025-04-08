from app import db
from library import *



class Vechuyenbay(db.Model):
    __tablename__ = 've_chuyen_bay'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Ma_chuyen_bay = db.Column(db.Integer, db.ForeignKey('chuyen_bay.id'), nullable = False)
    Ma_hanh_khach = db.Column(db.Integer, db.ForeignKey('hanh_khach.id'), nullable = True, default = None)
    hang_ve = db.Column(db.Integer)
    Tien_ve = db.Column(db.Float)
    Tinh_trang = db.Column(db.Boolean, default = False) # 0: da dat, 1: da huy
    vi_tri = db.Column(db.String(20))
    



    __table_args__ = (db.UniqueConstraint('Ma_chuyen_bay', 'vi_tri', name ='uq_machuyenbay_vitri'),) # Đảm bảo không có 2 vé giống nhau trong 1 chuyến bay

    def __repr__(self):
        return f"{self.Ma_chuyen_bay} - {self.hang_ve} - {self.vi_tri}"  # Sửa cách nối chuỗi
