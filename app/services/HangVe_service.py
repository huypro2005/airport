from app.models.HangVe import HangVe
from library import *


def add_hangve_service(data):
    """
    Thêm hạng vé mới vào cơ sở dữ liệu.
    :param data: Dữ liệu hạng vé cần thêm.
    :return: None
    """
    # Kiểm tra dữ liệu đầu vào
    if not data or 'Ten_hang_ve' not in data or 'Ti_le_don_gia' not in data:
        raise ValueError("Thiếu thông tin hạng vé!")
    
    # Tạo đối tượng HangVe mới
    hang_ve = HangVe(data['Ten_hang_ve'], data['Ti_le_don_gia'])
    
    # Thêm vào cơ sở dữ liệu
    try:
        db.session.add(hang_ve)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi khi thêm hạng vé: {str(e)}")
    
def get_ds_HangVe_service():
    """
    Lấy danh sách tất cả các hạng vé từ cơ sở dữ liệu.
    :return: Danh sách các hạng vé
    """
    try:
        hang_ve_list = HangVe.query.all()
        return hang_ve_list
    except Exception as e:
        raise ValueError(f"Lỗi khi lấy danh sách hạng vé: {str(e)}")