from app import db
from library import *


class PhieuDatCho(db.Model):
    __tablename__ = 'phieu_dat_cho'
    id = db.Column(db.Integer, primary_key=True)
    Ma_hanh_khach = db.Column(db.Integer, db.ForeignKey('hanh_khach.id'))
    Ma_cb = db.Column(db.Integer, db.ForeignKey('chuyen_bay.id'))
    Ngay_dat = db.Column(db.DateTime, default = datetime.now, index = True)
    Tinh_trang = db.Column(db.Integer) # 0: Da dat ve chua thanh toan, 1: Da thanh toan da nhan ve, 2: Da huy ve
    vi_tri = db.Column(db.String(20))
    # Ghi_chu = db.Column(db.String(100)) 
    hang_ve = db.Column(db.Integer)
    tra_tien = db.Column(db.Float)

    __table_args__ = (db.UniqueConstraint('Ma_cb', 'vi_tri', name = 'uq_mahanhkhach_machuyenbay_vitri'),)

    def __repr__(self):
        return f'{self.Ma_hanh_khach} - {self.Ma_vecb} - {self.Ma_chuyen_bay} - {self.Ngay_dat} - {self.Tinh_trang} - {self.Ghi_chu} - {self.tra_tien}'
    