from app import db
from sqlalchemy.orm import validates
from library import *



class Vechuyenbay(db.Model):
    __tablename__ = 'VECHUYENBAY'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Ma_chuyen_bay = db.Column(db.Integer, db.ForeignKey('CHUYENBAY.id'), nullable = False)
    Ma_hanh_khach = db.Column(db.Integer, db.ForeignKey('HANHKHACH.id'), nullable = True, default = None)
    Ma_hang_ve = db.Column(db.Integer, db.ForeignKey('HANGVE.id'), nullable = False)
    Ma_nhan_vien = db.Column(db.Integer, db.ForeignKey('NHANVIEN.id'), nullable = True, default = None)
    Ngay_dat_ve = db.Column(db.Date, nullable=True)
    Tien_ve = db.Column(db.Float)
    Tinh_trang = db.Column(db.Boolean, default = True) # 1: da dat, 0: da huy
    vi_tri = db.Column(db.String(20))
    


    def __repr__(self):
        return f"{self.Ma_chuyen_bay} - {self.hang_ve} - {self.vi_tri}"  # Sửa cách nối chuỗi

    @validates('Tinh_trang', 'vitri')
    def validate_seat(self, key, value):
        if key == 'Tinh_trang' and value is True:
            if Vechuyenbay.query.filter(
                Vechuyenbay.Ma_chuyen_bay == self.Ma_chuyen_bay,
                Vechuyenbay.Tinh_trang == True,
                Vechuyenbay.vi_tri == self.vi_tri,
                Vechuyenbay.id != self.id
            ).count() > 0:
                raise ValueError("Vị trí đã có người đặt.")
        return value