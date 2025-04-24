from app import db
from library import *


class HanhKhach(db.Model):
    __tablename__ = 'HANHKHACH'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Hoten = db.Column(db.String(50), nullable = False, index = True)
    cmnd = db.Column(db.String(30), nullable = False, unique = True)
    sdt = db.Column(db.String(15), nullable = False, unique = True)
    gioi_tinh = db.Column(db.String(10))
    vechuyenbay = db.relationship('Vechuyenbay', backref='hanh_khach', lazy=True)


    def __init__(self, Hoten, cmnd, sdt, gioi_tinh):
        self.Hoten = Hoten
        self.cmnd = cmnd
        self.sdt = sdt
        self.gioi_tinh = gioi_tinh



    def __repr__(self):
        return self.__Hoten
    
    def serialize(self):
        return {
            'id': self.id,
            'Hoten': self.Hoten,
            'cmnd': self.cmnd,
            'sdt': self.sdt,
            'gioi_tinh': self.gioi_tinh
        }