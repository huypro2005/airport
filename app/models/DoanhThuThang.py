from app import db
from library import *


class doanhThuThang(db.Model):
    __tablename__ = 'doanh_thu_thang'
    id = db.Column(db.Integer, primary_key=True)
    Tong_doanh_thu = db.Column(db.Float)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)

    
    def __repr__(self):
        return f'{self.Tong_doanh_thu} - {self.month} - {self.year}'
    