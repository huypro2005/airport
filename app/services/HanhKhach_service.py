from app.models.HanhKhach import HanhKhach
from library import *
from app.utils.validators import validate_HanhKhach


def add_hanh_khach(data):
    validate_HanhKhach(data)

    Hoten = data['Hoten']
    cmnd = data['cmnd']
    sdt = data['sdt']
    gioi_tinh = data.get('gioi_tinh', '')
    # ngaydangky = datetime.utcnow()
    try: 
        hanh_khach = HanhKhach(Hoten = Hoten, cmnd = cmnd, sdt = sdt, gioi_tinh = gioi_tinh)
        db.session.add(hanh_khach)
        db.session.commit()

    except Exception as e:
        raise ValueError(f"Lỗi: {e}")


def get_hanh_khach_by_id(id):
    try:
        hanh_khach = HanhKhach.query.get(id)
        if hanh_khach is None:
            raise ValueError("Không tìm thấy hành khách")
        return hanh_khach
    except Exception as e:
        raise ValueError(f"Lỗi: {e}")
    


