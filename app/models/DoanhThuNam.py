from app import db
from library import *


class doanhThuNam(db.Model):
    __tablename__ = "doanh_thu_nam"
    id = db.Column(db.Integer, primary_key = True)
    Tong_doanh_thu = db.Column(db.Float)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.Tong_doanh_thu} - {self.year}'
