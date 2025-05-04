import hmac
import hashlib
from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.FERNET_KEY)
HMAC_SECRET = settings.HMAC_SECRET.encode()

def encrypt(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt(data: str) -> str:
    return fernet.decrypt(data.encode()).decode()

def gHMAC(value: str) -> str:
    return hmac.new(HMAC_SECRET, value.encode(), hashlib.sha256).hexdigest()

def vHMAC(value: str, hmac_value: str) -> bool:
    expected_hmac = gHMAC(value)
    return hmac.compare_digest(expected_hmac, hmac_value)