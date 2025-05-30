from app.models.HanhKhach import HanhKhach
from library import *
from app.utils.validators import validate_HanhKhach


def add_hanh_khach(data):
    validate_HanhKhach(data)

    Hoten = data['Hoten']
    cmnd = data['cmnd']
    sdt = data['sdt']
    gioi_tinh = data.get('gioi_tinh', '')
    try:
        # Kiểm tra xem hành khách đã tồn tại chưa
        existing_hanh_khach_cmnd = HanhKhach.query.filter(cmnd==cmnd).first()

        if existing_hanh_khach_cmnd:
            raise ValueError("Hành khách đã tồn tại với CMND này")
        
        existing_hanh_khach_sdt = HanhKhach.query.filter(sdt==sdt).first()
        if existing_hanh_khach_sdt:
            raise ValueError("Hành khách đã tồn tại với số điện thoại này")
    except Exception as e:
        pass
        
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
    


'''

    {
        "Hoten": "Nguyen Van A",
        "cmnd": "1234567890",
        "sdt": "0909090909",
        "gioi_tinh": "Nam"
    }

'''

def add_or_get_HanhKhach_service(data):
    hanhkhach = HanhKhach.query.filter_by(cmnd=data['cmnd']).first()
    if hanhkhach:
        return hanhkhach
    else:
        try:
            hanhkhach = HanhKhach(
                Hoten=data['Hoten'],
                cmnd=data['cmnd'],
                sdt=data['sdt'],
                gioi_tinh=data['gioi_tinh']
            )
            db.session.add(hanhkhach)
            db.session.commit()
            return hanhkhach
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Lỗi: {e}")