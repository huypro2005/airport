from app import db
from library import *


class HangVe(db.Model):
    __tablename__ = 'HANGVE'
    id = db.Column(db.Integer, primary_key=True, index = True)
    Ten_hang_ve = db.Column(db.String(50), nullable = False, unique = True)
    Ti_le_don_gia = db.Column(db.Float, nullable = False)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, Ten_hang_ve, Ti_le_don_gia):
        self.Ten_hang_ve = Ten_hang_ve
        self.Ti_le_don_gia = Ti_le_don_gia

    def serialize(self):
        return {
            'id': self.id,
            'Ten_hang_ve': self.Ten_hang_ve,
            'Ti_le_don_gia': self.Ti_le_don_gia
        }