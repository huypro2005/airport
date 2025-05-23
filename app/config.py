import os
from re import S
from dotenv import load_dotenv
load_dotenv()


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT", "3306")}/{os.getenv("DB_NAME")}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:123456789@localhost:3306/airport?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ.get('KEY')  # Khóa bí mật của JWT
JWT_ACCESS_TOKEN_EXPIRES = 360000  # Thời gian sống của access token (100 giờ)
JWT_REFRESH_TOKEN_EXPIRES = 3600000  # Thời gian sống của refresh token (1000 giờ)
# config cors
CORS_HEADERS = 'Content-Type'
CORS_SUPPORTS_CREDENTIALS = True
# cho phép tất cả các nguồn gốc truy cập
CORS_ORIGINS = ['*']  # Hoặc có thể chỉ định các nguồn gốc cụ thể như ['http://localhost:3000']
CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']  # Các phương thức HTTP được phép