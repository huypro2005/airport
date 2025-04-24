from library import *
from app.models.DoanhThuThang import doanhThuThang
from app.models.Chuyenbay import Chuyenbay
from app.models.VeChuyenBay import Vechuyenbay
from .Chuyenbay_service import get_Chuyenbay_by_thang
from sqlalchemy import func



def get_doanh_thu_chuyenbay_all_by_thang_service(thang, nam):
    try:
        ds = get_Chuyenbay_by_thang(thang, nam)
        doanhthu = get_doanhthu_thang_service(thang, nam)
        data =[]
        for chuyenbay in ds:
            item = {}
            item['ma_chuyen_bay'] = chuyenbay.id
            item['doanh_thu'] = 0
            item['so_ve_ban'] = 0
            result = db.session.query(
                func.sum(Vechuyenbay.Tien_ve),
                func.count(Vechuyenbay.id)
            ).filter(
                Vechuyenbay.Ma_chuyen_bay == chuyenbay.id,
                Vechuyenbay.Tinh_trang == True
            ).first()
            item['doanh_thu'] = result[0] if result and result[0] is not None else 0
            item['so_ve_ban'] = result[1] if result and result[1] is not None else 0
            rate = item['doanh_thu'] / doanhthu.Tong_doanh_thu if doanhthu.Tong_doanh_thu > 0 else 0
            rate = round(rate, 2)
            item['rate'] = rate
            data.append(item)
        return data 
    except Exception as e:
        raise ValueError(f"Lỗi lấy doanh thu chuyến bay: {e}")


def get_doanhthu_thang_service(thang, nam):
    doanhThu = doanhThuThang.query.filter(doanhThuThang.month == thang, doanhThuThang.year == nam).first()
    return doanhThu
        


def create_doanhthu_thang_service(thang, nam):
    try:
        if doanhThuThang.query.filter(doanhThuThang.month == thang, doanhThuThang.year == nam).first():
            raise ValueError("Doanh thu tháng đã tồn tại")
        doanhthu = doanhThuThang()
        doanhthu.Tong_doanh_thu = 0
        doanhthu.month = thang
        doanhthu.year = nam
        ds = get_Chuyenbay_by_thang(thang, nam)
        tong_doanh_thu = 0
        so_chuyen_bay = 0
        tong_doanh_thu, so_chuyen_bay = db.session.query(
            func.sum(Vechuyenbay.Tien_ve),
            func.count(Vechuyenbay.id)
        ).filter(
            Vechuyenbay.Ma_chuyen_bay.in_(chuyenbay.id for chuyenbay in ds),
            Vechuyenbay.Tinh_trang == True
        ).first()
        doanhthu.Tong_doanh_thu = tong_doanh_thu
        doanhthu.so_chuyen_bay = so_chuyen_bay
        db.session.add(doanhthu)
        db.session.commit()
        return doanhthu
    except Exception as e:
        raise ValueError(f"Lỗi tạo doanh thu tháng: {e}")

def get_BaoCaoDoanhThuNam_service(nam):
    try:
        doanhThuNam = db.session.query(func.sum(doanhThuThang.Tong_doanh_thu)).filter(doanhThuThang.year == nam).scalar()
        if not doanhThuNam:
            raise ValueError("Không tìm thấy doanh thu năm")
        query = db.session.query(
            doanhThuThang.month,
            doanhThuThang.Tong_doanh_thu,
            doanhThuThang.Tong_doanh_thu,
            (doanhThuThang.Tong_doanh_thu/ doanhThuNam).label('rate')
        ).filter(
            doanhThuThang.year == nam
        )
        data = query.all()
        return {
            'data':[
                {
                    'thang': item.month,
                    'doanh_thu': item.Tong_doanh_thu,
                    'rate': item.rate
                }
                for item in data
            ],
            'doanh_thu_nam': doanhThuNam
        }
    except Exception as e:
        raise ValueError(f"Lỗi lấy báo cáo doanh thu năm: {e}")
    


