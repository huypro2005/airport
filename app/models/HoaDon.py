from app import db
from library import *
from app.models.VeChuyenBay import Vechuyenbay

class Hoadon(db.Model):
    __tablename__ = 'hoa_don'
    id = db.Column(db.Integer, primary_key=True)
    Ma_hanh_khach = db.Column(db.Integer, db.ForeignKey('hanh_khach.id'))
    Ma_ve_cb = db.Column(db.Integer, db.ForeignKey('ve_chuyen_bay.id'))
    Ma_nhan_vien = db.Column(db.Integer, db.ForeignKey('nhan_vien.id'), nullable = True)
    Loai_hoa_don = db.Column(db.Boolean, default = False) # 0: Thanh toan , 1: Hoan tien
    Ngay_lap = db.Column(db.DateTime, default = datetime.now)
    Thanh_tien = db.Column(db.Float)
    Ghi_chu = db.Column(db.String(100), nullable = True)


    def __repr__(self):
        return f'{self.Ma_hanh_khach} - {self.Ma_ve_cb} - {self.Ma_nhan_vien} - {self.Loai_hoa_don} - {self.Ngay_lap} - {self.Thanh_tien} - {self.Ghi_chu}'


    def Add_hoadon(self, vecb: Vechuyenbay):
        
        self.Ma_hanh_khach = vecb.Ma_hanh_khach
        self.Ma_ve_cb = vecb.id
        self.Thanh_tien = vecb.Tien_ve
        db.session.add(self)
        db.session.commit()

    
