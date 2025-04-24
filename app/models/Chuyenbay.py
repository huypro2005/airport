from app import db
from library import *



class Chuyenbay(db.Model):
    __tablename__ = 'CHUYENBAY'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Ma_san_bay_di = db.Column(db.String(20), db.ForeignKey('SANBAY.id'), nullable = False, index = True)     
    Ma_san_bay_den = db.Column(db.String(20), db.ForeignKey('SANBAY.id'), nullable = False, index = True)
    ngay_khoi_hanh = db.Column(db.Date)
    gio_khoi_hanh = db.Column(db.Time)
    Thoi_gian_bay = db.Column(db.Integer)
    gia_ve = db.Column(db.Float)
    # One to many relationship with ChiTietChuyenBay, PhieuDatCho, Vechuyenbay
    ve_chuyen_bay = db.relationship('Vechuyenbay', backref='chuyen_bay', lazy=True)
    chi_tiet_san_bay_trung_gian = db.relationship('ChiTietSanBayTrungGian', backref='chuyen_bay', lazy=True)

    def __repr__(self):
        return str(self.Ma_san_bay_di) + ' - ' + str(self.Ma_san_bay_den)
    

    def serialize(self):
        return {
            "Ma_chuyen_bay": self.id,
            "Ma_san_bay_di": self.Ma_san_bay_di,
            "Ma_san_bay_den": self.Ma_san_bay_den,
            "ngay_khoi_hanh": str(self.ngay_khoi_hanh),
            "gio_khoi_hanh": str(self.gio_khoi_hanh),
            "Thoi_gian_bay": self.Thoi_gian_bay,
            "gia_ve": self.gia_ve
        }