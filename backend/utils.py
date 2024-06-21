from uuid import uuid4
from base64 import urlsafe_b64encode

def short_uuid():
    uuid_bytes = uuid4().bytes
    uuid_base64 = urlsafe_b64encode(uuid_bytes).decode()
    return uuid_base64
