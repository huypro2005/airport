import datetime
from app.models import *

def validate_NgayGio(data):
    try:
        datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        raise ValueError("Ngày giờ không hợp lệ. Định dạng phải là YYYY-MM-DDTHH:MM:SS")
    
def format_NgayGio(data):
    return datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S')


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


def valadate_ChuyenBay(data, rule):

    required_fields = ['Ma_chuyen_bay', 'Ma_san_bay_di', 'Ma_san_bay_den', 
                       'Ma_may_bay', 'ngay_gio', 'thoi_gian_bay', 'gia_ve', 
                       'so_ghe_hang1', 'so_ghe_hang2']
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    
    if data['Ma_san_bay_di'] == data['Ma_san_bay_den']:
        raise ValueError("Mã sân bay đi và đến không được trùng")
    
    if data['thoi_gian_bay'] < rule.Thoigianbaytoithieu:
        raise ValueError(f"Thời gian bay phải lớn hơn {rule.Thoigianbaytoithieu} phút")
    
    if data['so_ghe_hang1'] < 0 or data['so_ghe_hang2'] < 0:
        raise ValueError("Số ghế không hợp lệ")
    
    if (data['Ma_chuyen_bay'] == '' or data['Ma_san_bay_di'] == '' or data['Ma_san_bay_den'] == '' or data['Ma_may_bay'] == ''
        or data['so_ghe_hang1'] == '' or data['so_ghe_hang2'] == ''
        or data['Ma_may_bay'] == '' or data['gia_ve'] == ''):
        raise ValueError("Các trường không được để trống")
    
    validate_NgayGio(data['ngay_gio'])
    ngay_gio = format_NgayGio(data['ngay_gio'])

    if ngay_gio < datetime.datetime.now():
        raise ValueError("Ngày giờ không hợp lệ")


def validate_SanBay(data):
    required_fields = ['Ma_san_bay', 'Ten_san_bay']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    if data['Ma_san_bay'] == '' or data['Ten_san_bay'] == '':
        raise ValueError("Các trường không được để trống")
    

def validate_MayBay(data):
    required_fields = ['Ma_may_bay', 'Ten_may_bay']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    
    if data['Ma_may_bay'] == '' or data['Ten_may_bay'] == '':
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
        

def validate_VeChuyenBay(data, rule):
    required_fields = ['Ma_chuyen_bay', 'Ho_ten', 'cmnd', 'sdt', 'gioi_tinh', 'hang_ve', 'vitri']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    if (data['Ma_chuyen_bay'] == '' or data['Ho_ten'] == '' or
         data['cmnd'] == '' or data['sdt'] == '' or 
         data['gioi_tinh'] == '' or data['hang_ve'] == '' or 
         data['vitri'] == ''):
        raise ValueError("Các trường không được để trống")
    
    if data['hang_ve'] not in [1, 2]:
        raise ValueError("Hạng vé không hợp lệ")
    
    
        

def validate_HanhKhach(data):
    required_fields = ['Hoten', 'cmnd', 'sdt']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}") 
        
            
            

def validate_PhieuDatCho(data, rule):
    required_fields = ['hoten', 'cmnd', 'sdt', 'gioi_tinh', 'machuyenbay', 'hangve', 'vi_tri']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    if data['hoten'] == '' or data['cmnd'] == '' or data['sdt'] == '' or data['gioi_tinh'] == '' or data['machuyenbay'] == '' or data['hangve'] == '' or data['vi_tri'] == '':
        raise ValueError("Các trường không được để trống")
    if data['hangve'] not in [1, 2]:
        raise ValueError("Hạng vé không hợp lệ")
    
    

def validate_Hoadon(data):
    required_fields = ['Ma_hanh_khach', 'Ma_ve_cb', 'Thanh_tien', 'Ghi_chu']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Thiếu trường bắt buộc: {field}")
    


def validate_NhanVien(data):
    required_fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'pos', 'position']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Thiếu trường bắt buộc: {field}')
    if data['id'] == '' or data['first_name'] == '' or data['last_name'] == '' or data['username'] == '' or data['password'] == '' or data['email'] == '' or data['pos'] == '' or data['position'] == '':
        raise ValueError("Các trường không được để trống")
    if data['pos'] not in [0, 1, 2]:
        raise ValueError("Chức vụ không hợp lệ")
    
