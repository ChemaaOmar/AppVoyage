from flask_cors import CORS

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    WTF_CSRF_METHODS = ["POST", "PUT", "PATCH", "DELETE"]
    CORS_ALLOW_HEADERS = ['Content-Type', 'X-CSRFToken']
    CORS_RESOURCES = {r"*": {"origins": "http://localhost:3000"}}
    SECURITY_MODE = True
