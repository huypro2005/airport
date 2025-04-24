from app import db
from library import *

class DoanhThuNam(db.Model):
    __tablename__ = 'DOANHTHUNAM'
    id = db.Column(db.Integer, primary_key=True)
    Tong_doanh_thu = db.Column(db.Float)
    year = db.Column(db.Integer)

    __table_args__ = (db.UniqueConstraint('year', name='uq_year'),)

    def __repr__(self):
        return f'{self.Tong_doanh_thu} - {self.year}'