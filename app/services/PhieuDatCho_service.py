from app.models.PhieuDatCho import PhieuDatCho
from app.models.HanhKhach import HanhKhach
from app.models.Chuyenbay import Chuyenbay
from app.models.HoaDon import Hoadon
from .QuyDinh_service import get_quydinh
from .Chuyenbay_service import set_sogheconlai, get_sogheconlai
from .VeChuyenBay_service import create_ve_through_phieudatcho_service
from .HoaDon_service import create_hoadon_through_vechuyenbay_service
from app.models.VeChuyenBay import Vechuyenbay
from app.utils.validators import validate_PhieuDatCho
from library import *




def get_phieu_dat_cho(id):
    try:
        phieudatcho = PhieuDatCho.query.get(id)
        hanhkhach = HanhKhach.query.get(phieudatcho.Ma_hanh_khach)
        return jsonify({
            'Ma_hanh_khach': phieudatcho.Ma_hanh_khach,
            'Hoten': hanhkhach.Hoten,
            'Ma_chuyen_bay': phieudatcho.Ma_cb,
            'Ngay_dat': phieudatcho.Ngay_dat,
            'Tinh_trang': phieudatcho.Tinh_trang,
            'Vi_tri': phieudatcho.vi_tri,
            'Hang_ve': phieudatcho.hang_ve,
            'Tra_tien': phieudatcho.tra_tien
        }), 200
    except Exception as e:
        error_message = traceback.format_exc()
        return jsonify({'message': f'Loi truy cap: {error_message}'}), 400
    

def add_phieudatcho(data):
    rule = get_quydinh()

    if rule is None:
        raise ValueError("Quy định không tồn tại")
    try:
        
        validate_PhieuDatCho(data, rule)

        hoten = data['hoten']
        cmnd = data['cmnd']
        sdt = data['sdt']
        gioi_tinh = data['gioi_tinh']
        machuyenbay = data['machuyenbay']
        hangve = data['hangve']
        vi_tri = data['vi_tri']
        
        

        ngaydat = datetime.utcnow()
        chuyenbay = Chuyenbay.query.get(machuyenbay)
        if chuyenbay is None:
            raise ValueError("Chuyến bay không tồn tại")
        
        if chuyenbay.ngay_gio - ngaydat < timedelta(days=1):
            raise ValueError("Chuyến bay đã gần đến giờ bay, không thể đặt vé")
        
        if get_sogheconlai(chuyenbay, hangve) == 0:
            raise ValueError("Chuyến bay đã hết chỗ")



        hanhkhach = HanhKhach.query.filter_by(cmnd = cmnd).first()
        if hanhkhach is None:
            hanhkhach= HanhKhach(Hoten = hoten, cmnd = cmnd, sdt = sdt, gioi_tinh = gioi_tinh)
            try:
                db.session.add(hanhkhach)
                db.session.commit()
            except Exception as e:
                raise ValueError(f"Lỗi thêm hành khách: {e}")

        
        set_sogheconlai(chuyenbay, hangve)

        if hangve == 1:
            giave = float(chuyenbay.gia_ve * rule.Phantramgia1 /100)
        else:
            giave = float(chuyenbay.gia_ve * rule.Phantramgia2 /100)
        tinhtrang = 0
        mahk = hanhkhach.id
        phieudatcho = PhieuDatCho(Ma_hanh_khach = mahk, 
                                Ma_cb = machuyenbay,
                                Ngay_dat = ngaydat, 
                                Tinh_trang = tinhtrang, 
                                hang_ve = hangve, 
                                tra_tien = giave, 
                                vi_tri = vi_tri)
        db.session.add(phieudatcho)
        db.session.commit()
        



    except Exception as e:
        db.session.rollback()
        error_message = traceback.format_exc()
        raise ValueError(f'Lỗi không xác định: {error_message}')
        # return jsonify({'message': ''}), 400
    

{
    "hoten" : "Cao Thanh Huy",
    "cmnd": "12456759",
    "sdt": "035264964",
    "gioi_tinh": "nam",
    "machuyenbay": 2,
    "hangve": 1,
    "vi_tri": "5.12"
}



def Thanhtoan_phieudatcho_services(id):
    try:
        
        Ma_phieu = id

        phieudatcho = PhieuDatCho.query.get(Ma_phieu)

        if phieudatcho is None:
            raise ValueError("Phiếu đặt chỗ không tồn tại")
                            
        if phieudatcho.Tinh_trang == 1:
            raise ValueError("Phiếu đặt chỗ đã thanh toán rồi")
        
        if phieudatcho.Tinh_trang == 2:
            raise ValueError("Phiếu đặt chỗ đã bị hủy")

        vechuyenbay = Vechuyenbay()

        phieudatcho.Tinh_trang = 1

        create_ve_through_phieudatcho_service(phieudatcho, vechuyenbay)
        try:
            db.session.add(vechuyenbay)
            db.session.commit()
        except Exception as e:
            raise ValueError(f"Lỗi: Không thể thêm vé chuyến bay")
        hoadon = Hoadon()
        create_hoadon_through_vechuyenbay_service(vechuyenbay, hoadon)
        try:
            db.session.add(hoadon)
            db.session.commit()
        except Exception as e:
            raise ValueError(f"Lỗi: Không thể thêm hóa đơn, hãy tạo hóa đơn thủ công")
        
    except ValueError as e:
        raise ValueError(f"Lỗi: {e}")


def get_ds_Phieudatcho_of_HK(mahk):
    try:
        ds = PhieuDatCho.query.filter_by(Ma_hanh_khach=mahk).all()
        data = []
        for phieudatcho in ds:
            data.append({
                'Ma_phieu': phieudatcho.id,
                'Ma_chuyen_bay': phieudatcho.Ma_cb,
                'Ngay_dat': phieudatcho.Ngay_dat,
                'Tinh_trang': phieudatcho.Tinh_trang,
                'Hang_ve': phieudatcho.hang_ve,
                'Ma_hanh_khach': phieudatcho.Ma_hanh_khach
            })
        return jsonify({'ds': data})
    except Exception as e:
        return jsonify({'message': f'Lỗi truy cập phiếu đặt chỗ: {e}'})
    
    
    
def get_Phieudatcho_by_Ma_cb(chuyenbay: Chuyenbay):
    try:
        ds_phieudatcho = chuyenbay.phieudatcho
        return ds_phieudatcho
    except Exception as e:
        raise ValueError(f"Lỗi: Không tìm thấy phiếu đặt chỗ")
    
def update_Phieudatcho_TinhTrang_Huy(phieudatcho: PhieuDatCho):
    phieudatcho.Tinh_trang = 2
    


def Huy_phieudatcho_through_chuyenbay_service(chuyenbay):
    try:
        phieudatcho = get_Phieudatcho_by_Ma_cb(chuyenbay)
        for phieudatcho in phieudatcho:
            update_Phieudatcho_TinhTrang_Huy(phieudatcho)
        db.session.commit()
    except Exception as e:
        raise ValueError(f"Lỗi: Không thể hủy phiếu đặt chỗ")



