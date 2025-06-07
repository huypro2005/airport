from app import db
from app.models.ChiTietHangVe import ChiTietHangVe
from library import *
from sqlalchemy import func


class Chuyenbay(db.Model):
    __tablename__ = 'CHUYENBAY'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Ma_san_bay_di = db.Column(db.String(20), db.ForeignKey('SANBAY.id'), nullable = False, index = True)     
    Ma_san_bay_den = db.Column(db.String(20), db.ForeignKey('SANBAY.id'), nullable = False, index = True)
    ngay_khoi_hanh = db.Column(db.Date)
    gio_khoi_hanh = db.Column(db.Time)
    Thoi_gian_bay = db.Column(db.Integer)
    gia_ve = db.Column(db.Float)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)
    # One to many relationship with ChiTietChuyenBay, PhieuDatCho, Vechuyenbay
    ve_chuyen_bay = db.relationship('Vechuyenbay', backref='chuyen_bay', lazy=True)
    chi_tiet_san_bay_trung_gian = db.relationship('ChiTietSanBayTrungGian', backref='chuyen_bay', lazy=True)
    chi_tiet_hang_ve = db.relationship('ChiTietHangVe', backref='chuyen_bay', lazy=True)
    def __repr__(self):
        return str(self.Ma_san_bay_di) + ' - ' + str(self.Ma_san_bay_den)
    

    def serialize(self):
        khoiHanh_datetime = datetime.combine(self.ngay_khoi_hanh, self.gio_khoi_hanh)
        self.thoiGianToi_datetime = khoiHanh_datetime + timedelta(minutes=self.Thoi_gian_bay)
        self.ngay_toi = self.thoiGianToi_datetime.date()
        self.gio_toi = self.thoiGianToi_datetime.time()
        try:
            so_ghe_dat, so_ghe_trong = db.session.query(
                func.sum(ChiTietHangVe.So_ve_da_dat).label('so_ghe_dat'), 
                func.sum(ChiTietHangVe.So_ve_trong).label('so_ghe_trong')
            ).filter(
                ChiTietHangVe.Ma_chuyen_bay == self.id
            ).first()
            if so_ghe_dat is None:
                so_ghe_dat = 0
            if so_ghe_trong is None:
                so_ghe_trong = 0
        except Exception as e:
            so_ghe_dat = 0
            so_ghe_trong = 0
            print(f"Error calculating seats: {e}")
        return {
            "Ma_chuyen_bay": self.id,
            "Ma_san_bay_di": self.Ma_san_bay_di,
            "Ma_san_bay_den": self.Ma_san_bay_den,
            "ngay_khoi_hanh": str(self.ngay_khoi_hanh),
            "gio_khoi_hanh": str(self.gio_khoi_hanh),
            "Thoi_gian_bay": self.Thoi_gian_bay,
            "ngay_toi": str(self.ngay_toi),
            "gio_toi": str(self.gio_toi),
            "gia_ve": self.gia_ve,
            "So_ghe_dat": int(so_ghe_dat),
            "So_ghe_trong": int(so_ghe_trong),
        }
    
    # def __dict__(self):
    #     return {
    #         "Ma_chuyen_bay": self.id,
    #         "Ma_san_bay_di": self.Ma_san_bay_di,
    #         "Ma_san_bay_den": self.Ma_san_bay_den,
    #         "ngay_khoi_hanh": str(self.ngay_khoi_hanh),
    #         "gio_khoi_hanh": str(self.gio_khoi_hanh),
    #         "Thoi_gian_bay": self.Thoi_gian_bay,
    #         "gia_ve": self.gia_ve,
    #     }



'''
select sum(so_ve_da_dat) as Tong_so_ve, sum(So_ve_trong) as Tong_so_ve_trong
from ChiTietHangVe c 
where c.Ma_chuyen_bay = 1

'''