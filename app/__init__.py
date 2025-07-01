from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from .vnpay.route import VNPAY_BLUEPRINT
from .extensions import db, migrate, jwt, cors
from .models import create_db
from .routes.Chuyenbay import CHUYENBAY
from .routes.SanBay import SANBAY
from .routes.HangVe import HANGVE
from .routes.VeChuyenBay import VECHUYENBAY
from .routes.HanhKhach import HANHKHACH
from .routes.NhanVien import NHANVIEN
from .routes.DoanhThuThang import DOANHTHUTHANG
from .routes.QuyDinh import QUYDINH
from .routes.ChiTiet_BCDTThang import CHITIETDOANHHTHUTHANG
from .routes.DoanhThuNam import DOANHTHUNAM
from .routes.auth import AUTH
from .services import SchedulerService

def create_app(file_config = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(file_config)
    create_db(app)

    with app.app_context():
        scheduler_service = SchedulerService()
        scheduler_service.run_daily()
        scheduler_service.start()

    jwt.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    app.register_blueprint(CHUYENBAY, url_prefix='/api')
    app.register_blueprint(SANBAY, url_prefix='/api')
    app.register_blueprint(HANGVE, url_prefix='/api')
    app.register_blueprint(VECHUYENBAY, url_prefix='/api')
    app.register_blueprint(HANHKHACH, url_prefix='/api')
    app.register_blueprint(NHANVIEN, url_prefix='/api')
    app.register_blueprint(QUYDINH, url_prefix='/api')
    app.register_blueprint(CHITIETDOANHHTHUTHANG, url_prefix='/api')
    app.register_blueprint(VNPAY_BLUEPRINT, url_prefix='/api')
    app.register_blueprint(DOANHTHUTHANG, url_prefix='/api')
    app.register_blueprint(AUTH, url_prefix='/api')
    app.register_blueprint(DOANHTHUNAM, url_prefix='/api')


    
    
    return app


