from email.policy import default
from app import db
from library import *



class QuyDinh(db.Model):
    __tablename__ = 'QUYDINH'
    id = db.Column(db.Integer, primary_key=True)
    Thoigianbaytoithieu = db.Column(db.Integer, default = 30)
    Soluongsanbaytrunggian = db.Column(db.Integer, default = 2)
    Thoigiandungtoithieu = db.Column(db.Integer, default = 10)
    Thoigiandungtoida = db.Column(db.Integer, default = 20)
    ThoiGianDatVeToiThieu = db.Column(db.Integer, default = 1) #Thoi gian dat ve muon nhat truoc luc chuyen bay khoi hanh, tinh theo gio
  
        
    def __repr__(self):
        return f'{self.Thoigianbaytoithieu} - {self.Soluongsanbaytrunggian} - {self.Thoigiandungtoithieu} - {self.Thoigiandungtoida} - {self.ThoiGianDatVeToiThieu}'
    def serialize(self):
        return {
            'thoigianbaytoithieu': self.Thoigianbaytoithieu,
            'soluongsanbaytrunggian': self.Soluongsanbaytrunggian,
            'thoigiandungtoithieu': self.Thoigiandungtoithieu,
            'thoigiandungtoida': self.Thoigiandungtoida,
            'thoigiandatvetoithieu': self.ThoiGianDatVeToiThieu
        }