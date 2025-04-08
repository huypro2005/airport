from app import db
from library import *



class Chuyenbay(db.Model):
    __tablename__ = 'chuyen_bay'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Ma_san_bay_di = db.Column(db.Integer, db.ForeignKey('san_bay.id'), nullable = False, index = True)     
    Ma_san_bay_den = db.Column(db.Integer, db.ForeignKey('san_bay.id'), nullable = False, index = True)
    Ma_may_bay = db.Column(db.Integer, db.ForeignKey('may_bay.id'), nullable = False)
    ngay_gio = db.Column(db.DateTime)
    Thoi_gian_bay = db.Column(db.Integer)
    gia_ve = db.Column(db.Integer)
    so_ghe_hang1 = db.Column(db.Integer)
    so_ghe_hang2 = db.Column(db.Integer)
    tong_so_ghe = db.Column(db.Integer)
    clear = db.Column(db.Boolean, default = False, nullable = True)
    # One to many relationship with ChiTietChuyenBay, PhieuDatCho, Vechuyenbay
    phieudatcho = db.relationship('PhieuDatCho', backref='chuyen_bay', lazy=True)
    ve_chuyen_bay = db.relationship('Vechuyenbay', backref='chuyen_bay', lazy=True)
    chi_tiet_chuyen_bay = db.relationship('ChiTietChuyenBay', backref='chuyen_bay', lazy=True)

    def __repr__(self):
        return str(self.Ma_san_bay_di) + ' - ' + str(self.Ma_san_bay_den)
    
