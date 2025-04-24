from app import db
from library import *

class ChiTietHangVe(db.Model):
    __tablename__ = 'CHITIETHANGVE'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Ma_hang_ve = db.Column(db.Integer, db.ForeignKey('HANGVE.id'), nullable=False)
    Ma_chuyen_bay = db.Column(db.Integer, db.ForeignKey('CHUYENBAY.id'), nullable=False)
    So_ve_trong = db.Column(db.Integer, nullable=False)
    So_ve_da_dat = db.Column(db.Integer, nullable=False)
    Gia_ve = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.Ma_hang_ve} - {self.Ma_chuyen_bay} - {self.So_ve_trong} - {self.So_ve_da_dat} - {self.Gia_ve}'