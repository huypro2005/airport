from app import db
from library import *



class QuyDinh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Soluongsanbay = db.Column(db.Integer, default = 10)
    Thoigianbaytoithieu = db.Column(db.Integer, default = 30)
    Soluongsanbaytrunggian = db.Column(db.Integer, default = 2)
    Thoigiandungtoithieu = db.Column(db.Integer, default = 10)
    Thoigiandungtoida = db.Column(db.Integer, default = 20)
    Phantramgia1 = db.Column(db.Float, default = 105)
    Phantramgia2 = db.Column(db.Float, default = 100)
    Time_max_phieu_het_han = db.Column(db.Integer, default = 1) # Thoi gian dat ve toi da
    
    # Soluonghangve = db.Column(db.Integer, default = 2)

        
    def __repr__(self):
        # return f'{self.Soluongsanbay} - {self.Thoigianbaytoithieu} - {self.Soluongsanbaytrunggian} - {self.Thoigiandungtoithieu} - {self.Thoigiandungtoida} - {self.Phantramgia1} - {self.Phantramgia2}'
        return f'So luong san bay: {self.Soluongsanbay} - Thoi gian bay toi thieu: {self.Thoigianbaytoithieu} - So luong san bay trung gian: {self.Soluongsanbaytrunggian} - Thoi gian dung toi thieu: {self.Thoigiandungtoithieu} - Thoi gian dung toi da: {self.Thoigiandungtoida} - Phan tram gia ve hang 1: {self.Phantramgia1} - Phan tram gia ve hang 2: {self.Phantramgia2}'
