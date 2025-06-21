from app.models.QuyDinh import QuyDinh
from library import *

def get_quydinh_service():
    """
    Hàm lấy quy định từ cơ sở dữ liệu.
    :return: Quy định hoặc raise ValueError nếu không tìm thấy
    """
    rule = QuyDinh.query.first()
    if not rule:
        raise ValueError("Không tìm thấy quy định")
    return rule



def update_quydinh_service(data):

    """
    Hàm cập nhật quy định trong cơ sở dữ liệu.
    :param data: Dữ liệu quy định cần cập nhật.
    :return: None

    {
        "soluongsanbaytrunggian": 3,
        "thoigianbaytoithieu": 30,
        "thoigiandungtoida": 20,
        "thoigiandungtoithieu": 10,
        "thoigianvechuyenbay": 1,
        "ThoiGianHuyVeToiDa": 5
    }
    """
    try:
        rule = QuyDinh.query.first()
        if not rule:
            raise ValueError("Không tìm thấy quy định")
        
        if data['thoigiandungtoida'] < data['thoigiandungtoithieu']:
            raise ValueError("Thời gian dừng tối đa không thể nhỏ hơn thời gian dừng tối thiểu")
        
        # Cập nhật các trường trong quy định
        rule.Thoigianbaytoithieu = data['thoigianbaytoithieu']
        rule.Soluongsanbaytrunggian = data['soluongsanbaytrunggian']
        rule.Thoigiandungtoida = data['thoigiandungtoida']
        rule.Thoigiandungtoithieu = data['thoigiandungtoithieu']
        rule.ThoiGianDatVeToiThieu = data['thoigianvechuyenbay']
        rule.ThoiGianHuyVeToiDa = data['ThoiGianHuyVeToiDa']
        # Lưu thay đổi vào cơ sở dữ liệu
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e