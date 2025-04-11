from library import *
from app.models.Maybay import Maybay


def add_Maybay(data):
    if data and 'ten_may_bay' in data:
        ten_may_bay = data['ten_may_bay']
        if Maybay.query.filter_by(ten_may_bay= ten_may_bay).first():
            raise ValueError("Máy bay đã tồn tại")
        try:
            maybay = Maybay(ten_may_bay= ten_may_bay)
            db.session.add(maybay)
            db.session.commit()
        except Exception as e:
            raise ValueError(f"Lỗi: {e}")
    else:   
        raise ValueError("Thiếu thông tin")



def get_Maybay_all():
    try:
        ds = Maybay.query.all()
        data = []
        for item in ds:
            data.append({
                'id': item.id,
                'ten_may_bay': item.ten_may_bay
            })
        return data
    except Exception as e:
        return None



def get_Maybay(id):
    maybay = Maybay.query.get(id)
    if maybay:
        return maybay
    return None

def delete_Maybay(id):
    maybay = Maybay.query.get(id)
    if maybay:
        try:
            db.session.delete(maybay)
            db.session.commit()
            
        except Exception as e:
            raise ValueError(f"Lỗi: {e}")
    raise ValueError("Không tìm thấy máy bay")


def update_Maybay(id,data):
    maybay = Maybay.query.get(id)
    if maybay:
        ten_may_bay = data['ten_may_bay']
        try:
            maybay.ten_may_bay = ten_may_bay
            db.session.commit()
        except Exception as e:
            raise ValueError(f"Lỗi: {e}")
    raise ValueError("Không tìm thấy máy bay")
