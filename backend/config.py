class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reservations.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mysecretkey'
    SECURITY_MODE = True  # True pour sécurisé, False pour non sécurisé
