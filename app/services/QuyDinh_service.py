from app.models.QuyDinh import QuyDinh
from library import *

def get_quydinh():
    """
    Hàm lấy quy định từ cơ sở dữ liệu.
    :return: Quy định hoặc raise ValueError nếu không tìm thấy
    """
    rule = QuyDinh.query.first()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    return rule




def update_quydinh_thoiGianBayToiThieu(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    rule.Thoigianbaytoithieu = data['Thoigianbaytoithieu']
    db.session.commit()



def update_quydinh_soLuongSanBayTrungGian(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    rule.Soluongsanbaytrunggian = data['Soluongsanbaytrunggian']
    db.session.commit()
    

def update_quydinh_thoiGianDungToiThieu(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    rule.Thoigiandungtoithieu = data['Thoigiandungtoithieu']
    db.session.commit()
    
def update_quydinh_thoiGianDungToiDa(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    rule.Thoigiandungtoida = data['Thoigiandungtoida']
    db.session.commit()



def update_quydinh_phanTramGiaVeHang1(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    rule.Phantramgia1 = data['Phantramgia1']
    db.session.commit()
    
    
def update_quydinh_phanTramGiaVeHang2(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    rule.Phantramgia2 = data['Phantramgia2']
    db.session.commit()


def update_quydinh_thoiGianDatVeToiDa(data):
    rule = get_quydinh()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    rule.Time_max_phieu_het_han = data['Time_max_phieu_het_han']
    db.session.commit()


