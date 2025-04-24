from library import *
from app.models.ChiTietSanBayTrungGian import ChiTietSanBayTrungGian
from app.models.Chuyenbay import Chuyenbay
from .QuyDinh_service import get_quydinh

def get_ds_ChiTietSanBayTrungGian_service(chuyenbay_id):  
    chuyenbay = Chuyenbay.query.get(chuyenbay_id)
    chitiets = chuyenbay.chi_tiet_san_bay_trung_gian

    return jsonify([ct.serialize() for ct in chitiets])
    
    
def update_Thoigiandung_CTSBTG_service(ctcb_id, Thoigiandung):
    try:
        ctcb = ChiTietSanBayTrungGian.query.get(ctcb_id)
        rule = get_quydinh()
        if not ctcb:
            raise ValueError("Chi tiết chuyến bay không tồn tại")
        
        if Thoigiandung < rule.Thoigiandungtoithieu or Thoigiandung > rule.Thoigiandungtoida:
            raise ValueError("Thời gian dừng không hợp lệ")
        ctcb.Thoi_gian_dung = Thoigiandung
        
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e