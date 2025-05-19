import datetime

from sqlalchemy import false
from app.models import *
import re




def validate_NgayGio(data):
    try:
        datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S')
    except ValueError as e:
        raise ValueError(f"Ngày giờ không hợp lệ. Định dạng phải là YYYY-MM-DDTHH:MM:SS : {e}")
    
    

def format_NgayGio(data):
    return datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S')

def format_Ngay(data):
    try:
        return datetime.datetime.strptime(data, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Định dạng ngày không hợp lệ. Định dạng phải là YYYY-MM-DD")

def format_Gio(data):
    try:
        return datetime.datetime.strptime(data, '%H:%M:%S').time()
    except ValueError:
        raise ValueError("Định dạng giờ không hợp lệ. Định dạng phải là HH:MM:SS")



def validate_timeRange(start_time_str, end_time_str):
    """
    Kiểm tra và chuyển đổi khoảng thời gian từ string sang datetime object.
    
    Args:
        start_time_str (str): Thời gian bắt đầu dạng string (YYYY-MM-DDTHH:MM:SS)
        end_time_str (str): Thời gian kết thúc dạng string (YYYY-MM-DDTHH:MM:SS)
        
    Returns:
        tuple: (datetime, datetime) - Tuple chứa start_time và end_time đã được chuyển đổi
        
    Raises:
        ValueError: Nếu định dạng thời gian không hợp lệ hoặc start_time > end_time
    """
    try:
        start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S')
        end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M:%S')

        if start_time > end_time:
            raise ValueError("Thời gian bắt đầu phải trước thời gian kết thúc")
        
        return start_time, end_time
    except ValueError:
        raise ValueError("Định dạng thời gian không hợp lệ")


'''
    {
    "Ma_chuyen_bay": 6,
    "Ma_san_bay_di": "HNOI",
    "Ma_san_bay_den": "SGON",
    "gia_ve": 500000,
    "ngay_khoi_hanh": "2025-04-25",
    "gio_khoi_hanh": "00:00:00",
    "thoi_gian_bay": 30,
    "chitiet":[
        {
            "Ma_san_bay_trung_gian": "DNANG",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 1"
        },
        {
            "Ma_san_bay_trung_gian": "Vinh",
            "thoigian_dung": 15,
            "ghichu": "Trung gian 2"
        }
    ],
    "hangve": [
        {
            "Ma_hang_ve": 1,
            "So_ghe_trong_hang": 50
        },
        {
            "Ma_hang_ve": 2,
            "So_ghe_trong_hang": 50
        }
    ]
}    


'''



def valadate_ChuyenBay(data, rule):

    required_fields = ['Ma_chuyen_bay', 'Ma_san_bay_di', 'Ma_san_bay_den', 'gia_ve', 'ngay_khoi_hanh', 'gio_khoi_hanh', 'thoi_gian_bay']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    if data['Ma_chuyen_bay'] == '' or data['Ma_san_bay_di'] == '' or data['Ma_san_bay_den'] == '' or data['gia_ve'] == '' or data['ngay_khoi_hanh'] == '' or data['gio_khoi_hanh'] == '' or data['thoi_gian_bay'] == '':
        raise ValueError("Các trường không được để trống")
    
    if data['Ma_san_bay_di'] == data['Ma_san_bay_den']:
        raise ValueError("Mã sân bay đi và đến không được giống nhau")
    
    if data['thoi_gian_bay'] < rule.Thoigianbaytoithieu:
        raise ValueError(f"Thời gian bay phải lớn hơn {rule.Thoigianbaytoithieu} phút")
    
    # Kiểm tra định dạng ngày giờ
    format_Ngay(data['ngay_khoi_hanh'])
    format_Gio(data['gio_khoi_hanh'])


def validate_SanBay(data):
    required_fields = ['Ma_san_bay', 'Ten_san_bay']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    if data['Ma_san_bay'] == '' or data['Ten_san_bay'] == '':
        raise ValueError("Các trường không được để trống")
    

def Validate_ChiTietChuyenBay(chitiet_list, rule, ma_san_bay_di, ma_san_bay_den):
    """
    Validator kiểm tra dữ liệu chi tiết chuyến bay.
    :param chitiet_list: Danh sách chi tiết chuyến bay
    :param rule: Quy định chuyến bay từ database
    :param ma_san_bay_di: Mã sân bay đi
    :param ma_san_bay_den: Mã sân bay đến
    :return: None nếu hợp lệ, hoặc raise ValueError nếu không hợp lệ
    """
    if not chitiet_list:
        return
    
    for chitiet in chitiet_list:
        ma_san_bay_trung_gian = chitiet.get('Ma_san_bay_trung_gian')
        thoi_gian_dung = chitiet.get('thoigian_dung')
        ghichu = chitiet.get('ghichu')
        if not ma_san_bay_trung_gian or not thoi_gian_dung :
            raise ValueError("Thiếu thông tin mã sân bay trung gian hoặc thời gian dừng")

        if ma_san_bay_trung_gian == ma_san_bay_di or ma_san_bay_trung_gian == ma_san_bay_den:
            raise ValueError("Mã sân bay trung gian không hợp lệ")
        if thoi_gian_dung < rule.Thoigiandungtoithieu or thoi_gian_dung > rule.Thoigiandungtoida:
            raise ValueError(f"Thời gian dừng tại sân bay trung gian phải từ {rule.Thoigiandungtoithieu} đến {rule.Thoigiandungtoida} phút")
        


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

def validate_VeChuyenBay(data, rule):
    required_fields = ['Ma_chuyen_bay', 'Ho_ten', 'cmnd', 'sdt', 'gioi_tinh', 'Ma_hang_ve', 'vitri']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    if (data['Ma_chuyen_bay'] == '' or data['Ho_ten'] == '' or
         data['cmnd'] == '' or data['sdt'] == '' or 
         data['gioi_tinh'] == '' or data['Ma_hang_ve'] == '' or 
         data['vitri'] == ''):
        raise ValueError("Các trường không được để trống")
    
    

    
    
def validate_VeChuyenBay_seat(vitri, Ma_chuyen_bay):
    count = Vechuyenbay.query.filter(
        Vechuyenbay.vi_tri == vitri,
        Vechuyenbay.Ma_chuyen_bay == Ma_chuyen_bay,
        Vechuyenbay.Tinh_trang == True
    ).count()
    if count > 0:
        raise ValueError("Ghế đã được đặt")
    
    

        

def validate_HanhKhach(data):
    required_fields = ['Hoten', 'cmnd', 'sdt']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}") 
        
    if data['Hoten'] == '' or data['cmnd'] == '' or data['sdt'] == '':
        raise ValueError("Các trường không được để trống")
    

        

'''
{
        "Ma_chuyen_bay": 1,
        "hang_ve": 1,
        "vitri": "B4.1",
        "Ho_ten": "nguyen van a",
        "cmnd": "116468466314",
        "sdt": "24544346",
        "gioi_tinh": "Nam"
    }
'''
            
            

def validate_PhieuDatCho(data, rule):
    required_fields = ['Ho_ten', 'cmnd', 'sdt', 'gioi_tinh', 'Ma_chuyen_bay', 'hang_ve', 'vitri']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    if data['Ho_ten'] == '' or data['cmnd'] == '' or data['sdt'] == '' or data['gioi_tinh'] == '' or data['Ma_chuyen_bay'] == '' or data['hang_ve'] == '' or data['vitri'] == '':
        raise ValueError("Các trường không được để trống")
    if data['hang_ve'] not in [1, 2]:
        raise ValueError("Hạng vé không hợp lệ")
    
    

def validate_Hoadon(data):
    required_fields = ['Ma_hanh_khach', 'Ma_ve_cb', 'Thanh_tien', 'Ghi_chu']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    


def validate_NhanVien(data):
    required_fields = ['id', 'name', 'username', 'password', 'email',  'position']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Thiếu trường bắt buộc: {field}')
    if data['id'] == '' or data['name'] == '' or data['username'] == '' or data['password'] == '' or data['email'] == '' or data['pos'] == '' or data['position'] == '':
        raise ValueError("Các trường không được để trống")
    if data['pos'] not in [0, 1, 2]:
        raise ValueError("Chức vụ không hợp lệ")
    
