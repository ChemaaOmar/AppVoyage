from flask_limiter.util import get_remote_address
from models import SecurityMode

def limit_key_func():
    security_mode = SecurityMode.query.first().mode
    if security_mode == 'secure':
        return get_remote_address()
    else:
        return None
