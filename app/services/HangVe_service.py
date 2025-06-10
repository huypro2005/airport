from app.models.ChiTietHangVe import ChiTietHangVe
from app.models.Chuyenbay import Chuyenbay
from app.models.HangVe import HangVe
from library import *

def check_hangve_active(id):
    """
    Kiểm tra xem hạng vé có đang hoạt động hay không.
    :param id: ID của hạng vé cần kiểm tra.
    :return: True nếu hạng vé đang hoạt động, False nếu không.
    """
    hangve = HangVe.query.filter_by(id=id, is_deleted=False).first()
    return hangve is not None


def add_hangve_service(data):
    """
    Thêm hạng vé mới vào cơ sở dữ liệu.
    :param data: Dữ liệu hạng vé cần thêm.
    :return: None
    """
    # Kiểm tra dữ liệu đầu vào
    if not data or 'Ten_hang_ve' not in data or 'Ti_le_don_gia' not in data:
        raise ValueError("Thiếu thông tin hạng vé!")
    
    hangve = HangVe.query.filter(HangVe.Ten_hang_ve == data['Ten_hang_ve']).first()
    if hangve:
        raise ValueError("Hạng vé đã tồn tại")

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
        hang_ve_list = HangVe.query.filter_by(is_deleted=False).all()
        if not hang_ve_list:
            raise ValueError("Không có hạng vé nào trong cơ sở dữ liệu")
        return hang_ve_list
    except Exception as e:
        raise ValueError(f"Lỗi khi lấy danh sách hạng vé: {str(e)}")
    


def update_hangve_service(id, data):
    try:
        hangve = HangVe.query.filter_by(id=id, is_deleted=False).first()
        if not hangve:
            raise ValueError("Không tìm thấy hạng vé")
        
        # Validate dữ liệu đầu vào
        if 'Ten_hang_ve' in data:
            hangve.Ten_hang_ve = data['Ten_hang_ve']
        if 'Ti_le_don_gia' in data:
            hangve.Ti_le_don_gia = data['Ti_le_don_gia']
            db.session.query(ChiTietHangVe).filter(
                ChiTietHangVe.Ma_hang_ve == hangve.id
            ).update({
                ChiTietHangVe.Gia_ve: data['Ti_le_don_gia']*float(
                    db.session.query(Chuyenbay).filter(
                        Chuyenbay.id == ChiTietHangVe.Ma_chuyen_bay
                    ).first().gia_ve
                )
            })
        
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi không xác định: {e}")
    

def delete_hangve_service(id):
    try:
        hangve = HangVe.query.filter_by(id=id, is_deleted=False).first()
        if not hangve:
            raise ValueError("Không tìm thấy hạng vé")

        hangve.is_deleted = True
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        raise ValueError(f"{e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Lỗi không xác định: {e}")