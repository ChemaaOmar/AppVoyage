class Config:
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reservations.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    WTF_CSRF_METHODS = ["POST", "PUT", "PATCH", "DELETE"]  # Assurez-vous que les méthodes sont correctes
    SECURITY_MODE = True
    CORS_ALLOW_HEADERS = ['Content-Type', 'X-CSRFToken']  # Ajoutez ici
    CORS_RESOURCES = {r"*": {"origins": "http://localhost:3000"}}  # Ajoutez ici