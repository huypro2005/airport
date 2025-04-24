from app import db
from library import *


class ChiTietSanBayTrungGian(db.Model):
    __tablename__ = 'CHITIETSANBAYTRUNGGIAN'
    id = db.Column(db.Integer, primary_key=True)
    Ma_chuyen_bay = db.Column(db.Integer, db.ForeignKey('CHUYENBAY.id'))
    Ma_san_bay_trung_gian = db.Column(db.String(20), db.ForeignKey('SANBAY.id'))
    Thoi_gian_dung = db.Column(db.Integer)
    Ghi_chu = db.Column(db.String(100), nullable = True)

    def __repr__(self):
        return f'{self.Ma_chuyen_bay} - {self.Ma_san_bay_trung_gian}'
    
    def serialize(self):
        return {
            'ma_chuyen_bay': self.Ma_chuyen_bay,
            'ma_san_bay_trung_gian': self.Ma_san_bay_trung_gian,
            'thoi_gian_dung': self.Thoi_gian_dung,
            'ghi_chu': self.Ghi_chu
        }