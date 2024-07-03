from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_limiter import Limiter
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
cors = CORS()
limiter = Limiter(key_func=lambda: 'global_limit')  # ou get_remote_address si configuré
csrf = CSRFProtect()
