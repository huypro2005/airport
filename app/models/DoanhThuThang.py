from app import db
from library import *


class doanhThuThang(db.Model):
    __tablename__ = 'DOANHTHUTHANG'
    id = db.Column(db.Integer, primary_key=True)
    Tong_doanh_thu = db.Column(db.Float)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    so_chuyen_bay = db.Column(db.Integer)
    Tile = db.Column(db.Float)


    __table_args__ = (db.UniqueConstraint('month', 'year', name = 'uq_month_year'),)
    
    def __repr__(self):
        return f'{self.Tong_doanh_thu} - {self.month} - {self.year}'