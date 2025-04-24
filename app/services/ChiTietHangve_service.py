from app.models.ChiTietHangVe import ChiTietHangVe
from app import db

'''

{
    "Ma_hang_ve": 1,
    "Ma_chuyen_bay": 1,
    "So_ve_trong": 100,
    "So_ve_da_dat": 50,
    "Gia_ve": 2000000

}

'''

def add_ChiTietHangVe_service(data):
    ma_hang_ve = data['Ma_hang_ve']
    ma_chuyen_bay = data['Ma_chuyen_bay']
    so_ve_trong = data['So_ve_trong']
    so_ve_da_dat = data['So_ve_da_dat']
    gia_ve = data['Gia_ve']

    # Kiểm tra xem chi tiết hàng vé đã tồn tại chưa
    existing_record = ChiTietHangVe.query.filter_by(Ma_hang_ve=ma_hang_ve, Ma_chuyen_bay=ma_chuyen_bay).first()
    if existing_record:
        raise ValueError("Chi tiết hàng vé đã tồn tại")

    # Tạo mới chi tiết hàng vé
    new_record = ChiTietHangVe(
        Ma_hang_ve=ma_hang_ve,
        Ma_chuyen_bay=ma_chuyen_bay,
        So_ve_trong=so_ve_trong,
        So_ve_da_dat=so_ve_da_dat,
        Gia_ve=gia_ve
    )

    try:
        db.session.add(new_record)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    

def get_ChiTietHangVe_servicel(MaChuyenBay, MaHangVe):
    # Kiểm tra xem chi tiết hàng vé đã tồn tại chưa
    existing_record = ChiTietHangVe.query.filter_by(Ma_hang_ve=MaHangVe, Ma_chuyen_bay=MaChuyenBay).first()
    if existing_record:
        return existing_record
    else:
        return None