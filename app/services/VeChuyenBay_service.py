from cv2 import add
from app.models.VeChuyenBay import Vechuyenbay
from app.models.Chuyenbay import Chuyenbay
from app.models.HanhKhach import HanhKhach
from .QuyDinh_service import get_quydinh
from .Chuyenbay_service import get_sogheconlai, set_sogheconlai
from .HanhKhach_service import add_or_get_HanhKhach_service
from app.utils.validators import validate_VeChuyenBay,  validate_VeChuyenBay_seat
from library import *



'''

    {
        "Ma_chuyen_bay": 1,
        "Ma_hang_ve": 1,
        "vitri": "B4.1",
        "Ho_ten": "nguyen van a",
        "cmnd": "116468466314",
        "sdt": "24544346",
        "gioi_tinh": "Nam"
    }

'''


def add_veChuyenyBay_service(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Lỗi truy cập quy định.")
    try:
        validate_VeChuyenBay(data, rule)
        macb = data['Ma_chuyen_bay']
        Hoten = data['Ho_ten']
        cmnd = data['cmnd']
        sdt = data['sdt']
        gioi_tinh = data['gioi_tinh']
        hang_ve = data['Ma_hang_ve']
        vitri = data['vitri']
        
        validate_VeChuyenBay_seat(vitri, macb)
        data = {
            'Hoten': Hoten,
            'cmnd': cmnd,
            'sdt': sdt,
            'gioi_tinh': gioi_tinh
        }
        add_or_get_HanhKhach_service(data)



    except:
        pass
        



{
    "Ma_chuyen_bay": 1,
    "Ho_ten" : "Dau Thi Vy",
    "cmnd": "234556456",
    "sdt": "546362",
    "gioi_tinh": "Nu",
    "hang_ve": 1,
    "vitri": "B5.1"
}   




def get_veChuyenBay_byID_service(id):
    ve_chuyen_bay = Vechuyenbay.query.get(id)
    if ve_chuyen_bay:
        return ve_chuyen_bay
    else:
        return None




def delete_ve_service(id):
    ve = Vechuyenbay.query.get(id)
    if ve:
        db.session.delete(ve)
        db.session.commit()
    else:
        raise ValueError("Không tìm thấy vé")

def giave_chuyenbay_follow_hangve_service(chuyenbay: Chuyenbay, hangve: int):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Lỗi truy cập quy định.")
    if hangve == 1:
        return chuyenbay.gia_ve * rule.Phantramgia1/100
    else:
        return chuyenbay.gia_ve * rule.Phantramgia2/100

