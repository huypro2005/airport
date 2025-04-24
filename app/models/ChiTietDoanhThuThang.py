from app import db 
from library import *

class ChiTietDoanhThuThang(db.Model):
    __fsa__tablename__ = 'CHITIETDOANHTHUTHANG'
    id = db.Column(db.Integer, primary_key=True)
    Ma_BCDTT = db.Column(db.Integer, db.ForeignKey('DOANHTHUTHANG.id'), nullable=False)
    Ma_chuyen_bay = db.Column(db.Integer, db.ForeignKey('CHUYENBAY.id'), nullable=False)
    Tong_so_ve = db.Column(db.Integer, nullable=False)
    Ti_le = db.Column(db.Float, nullable=False)
    Doanh_thu = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.Ma_BCDTT} - {self.Ma_chuyen_bay} - {self.Tong_so_ve} - {self.Ti_le} - {self.Doanh_thu}'
    def __init__(self, Ma_BCDTT, Ma_chuyen_bay, Tong_so_ve, Ti_le, Doanh_thu):
        self.Ma_BCDTT = Ma_BCDTT
        self.Ma_chuyen_bay = Ma_chuyen_bay
        self.Tong_so_ve = Tong_so_ve
        self.Ti_le = Ti_le
        self.Doanh_thu = Doanh_thu