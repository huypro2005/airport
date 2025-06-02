from app import db 
from library import *

class ChiTietDoanhThuThang(db.Model):
    __fsa__tablename__ = 'CHITIETDOANHTHUTHANG'
    id = db.Column(db.Integer, primary_key=True)
    Ma_BCDTT = db.Column(db.Integer, db.ForeignKey('DOANHTHUTHANG.id'), nullable=True)
    thang = db.Column(db.Integer, nullable=False)
    nam = db.Column(db.Integer, nullable=False)
    Ma_chuyen_bay = db.Column(db.Integer, db.ForeignKey('CHUYENBAY.id'), nullable=False)
    So_ghe_dat = db.Column(db.Integer, nullable=False)
    Ti_le = db.Column(db.Float, nullable=False)
    Doanh_thu = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.Ma_BCDTT} - {self.Ma_chuyen_bay} - {self.Tong_so_ve} - {self.Ti_le} - {self.Doanh_thu}'
    
    def serialize(self):
        return {
            'thang': self.thang,
            'nam': self.nam,
            'Ma_chuyen_bay': self.Ma_chuyen_bay,
            'So_ghe_dat': self.So_ghe_dat,
            'Ti_le': self.Ti_le,
            'Doanh_thu': self.Doanh_thu,
        }