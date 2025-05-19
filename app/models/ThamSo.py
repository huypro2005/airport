from app import db
from library import *


class ThamSo(db.Model):
    __tablename__ = 'THAMSO'
    id = db.Column(db.Integer, primary_key=True)
    TenThamSo = db.Column(db.String(255), nullable=False)
    GiaTri = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.TenThamSo} - {self.GiaTri}'
    def serialize(self):
        return {
            'ten_tham_so': self.TenThamSo,
            'gia_tri': self.GiaTri
        }

