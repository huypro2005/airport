import os
from dotenv import load_dotenv
load_dotenv()


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:123456789@localhost:3306/airport?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('KEY')  # Khóa bí mật của ứng dụng