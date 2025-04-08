from app import db
from library import *



class Nhanvien(db.Model):
    __tablename__ = 'nhan_vien'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.Text)
    email = db.Column(db.String(120), unique = True)
    pos = db.Column(db.Integer)# 0: Nhan vien, 1: Quan ly, 2: Admin
    position = db.Column(db.String(50)) # Chuc vu
    tinhtrang = db.Column(db.Boolean, default = True) # 0: Da nghi viec, 1: Con lam viec


    def __repr__(self):
        return self.name