from app import db
from library import *


class Sanbay(db.Model):
    __tablename__ = 'SANBAY'
    id = db.Column(db.String(20), primary_key=True, index = True)
    ten_san_bay = db.Column(db.String(50), nullable = False, index = True, unique= True)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return self.ten_san_bay
    
    def serialize(self):
        return {
            'id': self.id,
            'ten_san_bay': self.ten_san_bay
        }