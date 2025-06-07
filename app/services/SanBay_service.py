from app.models.SanBay import Sanbay
from library import *
from app.utils.validators import validate_SanBay



def check_SanBay_Active(ma_san_bay):
    sanbay = Sanbay.query.filter_by(id=ma_san_bay, is_deleted=False).first()
    if not sanbay:
        return False
    return True


def add_SanBay_service(data):
    validate_SanBay(data)
    # quydinh = get_quydinh()


    ma_san_bay = data['Ma_san_bay']
    ten_san_bay = data['Ten_san_bay']
    
    sanbay = Sanbay.query.get(ma_san_bay)
    if sanbay:
        raise ValueError("Mã sân bay đã tồn tại")
    
    sanbay = Sanbay(id=ma_san_bay, ten_san_bay=ten_san_bay)
    
    try:
        db.session.add(sanbay)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e 


{
    "Ma_san_bay": "SGN",
    "Ten_san_bay": "Sân bay Tân Sơn Nhất"
}

def get_ds_sanbay_service():
    ds_sanbay = Sanbay.query.filter_by(is_deleted=False).all()
    if not ds_sanbay:
        raise ValueError("Không có sân bay nào trong cơ sở dữ liệu")
    return ds_sanbay

def get_sanbay_by_id_service(ma_san_bay):
    sanbay = Sanbay.query.filter_by(id=ma_san_bay, is_deleted=False).first()
    if sanbay:
        return sanbay
    return None

def delete_sanbay_service(ma_san_bay):
    sanbay = Sanbay.query.filter_by(id=ma_san_bay, is_deleted=False).first()
    if sanbay:
        sanbay.is_deleted = True
        db.session.commit()
    else:
        raise ValueError("Sân bay không tồn tại")

def update_sanbay_service(ma_san_bay, data):
    sanbay = Sanbay.query.filter_by(id=ma_san_bay, is_deleted=False).first()
    if sanbay:
        sanbay.ten_san_bay = data['ten_san_bay']
        db.session.commit()
    else:
        raise ValueError("Sân bay không tồn tại")





