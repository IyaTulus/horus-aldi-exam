import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '')
    DB_NAME = os.getenv('DB_NAME', 'horus_aldi_db')
    
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
    )
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_EXPIRES', 900))  # in seconds
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_EXPIRES', 2592000))  # in seconds
    
    JWT_TOKEN_LOCATION = os.getenv('JWT_TOKEN_LOCATION', 'headers')
    
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = True
    