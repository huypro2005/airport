from .DoanhThuNam_service import create_or_update_doanhthu_nam_service, create_or_update_doanhthu_thang_service
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

class SchedulerService:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def start(self):
        # Lên lịch chạy hàng ngày lúc 00:00
        self.scheduler.add_job(self.run_daily, 'cron', hour=23, minute=59)
        self.scheduler.start()

    def run_daily(self):
        try:
            today = datetime.now()
            year = today.year
            month = today.month
            create_or_update_doanhthu_thang_service(month, year)
            create_or_update_doanhthu_nam_service(year)
            print(f"Daily job executed successfully on {today.strftime('%Y-%m-%d')}")
        except Exception as e:
            print(f"Error in daily job: {e}")