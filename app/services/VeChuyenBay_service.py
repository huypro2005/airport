from app.models.VeChuyenBay import Vechuyenbay
from app.models.Chuyenbay import Chuyenbay
from app.models.HanhKhach import HanhKhach
from app.models.HoaDon import Hoadon
from app.models.PhieuDatCho import PhieuDatCho
from .QuyDinh_service import get_quydinh
from .Chuyenbay_service import get_sogheconlai, set_sogheconlai
from .HoaDon_service import create_Hoadon_hoantien_service, create_Hoadon_themtien_service
from app.utils.validators import validate_VeChuyenBay
from library import *



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
        hang_ve = data['hang_ve']
        vitri = data['vitri']
        ma_hanh_khach =None
        

        hanhkhach = HanhKhach.query.filter_by(cmnd = cmnd).first()
        
        if hanhkhach:
            ma_hanh_khach = hanhkhach.id
        else:
            hanhkhach = HanhKhach(Hoten= Hoten, cmnd = cmnd, sdt = sdt, gioi_tinh = gioi_tinh)
            try:
                db.session.add(hanhkhach)
                db.session.commit()
            except ValueError as e:
                db.session.rollback()
                raise ValueError(f"Lỗi tạo hành khách: {e}")
            ma_hanh_khach = hanhkhach.id
        
        if ma_hanh_khach is None:
            raise ValueError("Lỗi truy cập hành khách")  
        giave =0
        chuyenbay = Chuyenbay.query.filter_by(id = macb).first()

        if not chuyenbay:
            return jsonify({'message': 'Mã chuyến bay không hợp lệ'}), 400
        
        if get_sogheconlai(chuyenbay, hang_ve) == 0:
            raise ValueError("Hết vé")
        
        if hang_ve == 1:
            giave = chuyenbay.gia_ve * rule.Phantramgia1/100
        else:
            giave = chuyenbay.gia_ve * rule.Phantramgia2/100
        
        ve = Vechuyenbay(Ma_chuyen_bay = macb, Ma_hanh_khach = ma_hanh_khach, hang_ve = hang_ve, vi_tri = vitri, Tien_ve = giave)
        try:
            db.session.add(ve)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Đặt vé thất bại: {e}")
        
        set_sogheconlai(chuyenbay, hang_ve)


        hoadon = Hoadon()
        try:
            hoadon.Add_hoadon(ve)
            db.session.commit()
            return ve
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Lỗi tạo hóa đơn khi vé đã được đặt: {e}")
       

        
    except Exception as e:
       raise ValueError(f"Lỗi: {e}")
    


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



def create_ve_through_phieudatcho_service(phieudatcho: PhieuDatCho, vechuyenbay: Vechuyenbay):
    vechuyenbay.Ma_chuyen_bay = phieudatcho.Ma_cb
    vechuyenbay.Ma_hanh_khach = phieudatcho.Ma_hanh_khach
    vechuyenbay.hang_ve = phieudatcho.hang_ve
    vechuyenbay.Tien_ve = phieudatcho.tra_tien
    vechuyenbay.vi_tri = phieudatcho.vi_tri
    


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

def update_ve_Hangve_service(vechuyenbay_id, hangve):
    
    try:
        vechuyenbay = Vechuyenbay.query.get(vechuyenbay_id)
        if not vechuyenbay:
            raise ValueError("Không tìm thấy vé")
        vechuyenbay.hang_ve = hangve
        chuyenbay = vechuyenbay.chuyen_bay
        giave = giave_chuyenbay_follow_hangve_service(chuyenbay, hangve)

        hoadon = Hoadon()
        if giave > vechuyenbay.Tien_ve:
            hoadon.Thanh_tien = giave - vechuyenbay.Tien_ve
            create_Hoadon_themtien_service(vechuyenbay, hoadon)
            
        else:
            hoadon.Thanh_tien = vechuyenbay.Tien_ve - giave
            create_Hoadon_hoantien_service(vechuyenbay, hoadon)
        
        vechuyenbay.Tien_ve = giave
        db.session.add(hoadon)
        db.session.commit()
    except Exception as e:
        raise ValueError(f"Lỗi cập nhật vé: {e}")

def update_huy_ve_service(vechuyenbay_id):
    try:
        vechuyenbay = Vechuyenbay.query.get(vechuyenbay_id)
        if not vechuyenbay:
            raise ValueError("Không tìm thấy vé")
        vechuyenbay.Tinh_trang = True
        hoadon = Hoadon()
        hoadon.Thanh_tien = vechuyenbay.Tien_ve
        create_Hoadon_hoantien_service(vechuyenbay, hoadon)
        db.session.add(hoadon)
        db.session.commit()
    except Exception as e:
        raise ValueError(f"Lỗi hủy vé: {e}")
    

