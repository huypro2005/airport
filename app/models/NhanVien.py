from app import db
from library import *



class Nhanvien(db.Model):
    __tablename__ = 'NHANVIEN'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.Text)
    email = db.Column(db.String(120), unique = True)
    position = db.Column(db.String(50)) # Chuc vu
    tinhtrang = db.Column(db.Boolean, default = True) # 0: Da nghi viec, 1: Con lam viec


    def __repr__(self):
        return self.name
    

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'position': self.position,
            'tinhtrang': self.tinhtrang
        }