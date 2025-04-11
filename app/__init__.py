from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .extensions import db, migrate, jwt
from .models import create_db
from .routes.Chuyenbay import CHUYENBAY
from .routes.SanBay import SANBAY
from .routes.VeChuyenBay import VECHUYENBAY
from .routes.HanhKhach import HANHKHACH
from .routes.Maybay import MAYBAY
from .routes.PhieuDatCho import PHIEUDATCHO
from .routes.HoaDon import HOADON
from .routes.NhanVien import NHANVIEN
from .routes.DoanhThuThang import DOANHTHUTHANG
from .routes.QuyDinh import QUYDINH
from .routes.auth import AUTH

def create_app(file_config = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(file_config)
    create_db(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(CHUYENBAY, url_prefix='/api')
    app.register_blueprint(SANBAY, url_prefix='/api')
    app.register_blueprint(VECHUYENBAY, url_prefix='/api')
    app.register_blueprint(HANHKHACH, url_prefix='/api')
    app.register_blueprint(MAYBAY, url_prefix='/api')
    app.register_blueprint(PHIEUDATCHO, url_prefix='/api')
    app.register_blueprint(HOADON, url_prefix='/api')
    app.register_blueprint(NHANVIEN, url_prefix='/api')
    app.register_blueprint(QUYDINH, url_prefix='/api')
    app.register_blueprint(DOANHTHUTHANG, url_prefix='/api')
    app.register_blueprint(AUTH, url_prefix='/api')
    return app


