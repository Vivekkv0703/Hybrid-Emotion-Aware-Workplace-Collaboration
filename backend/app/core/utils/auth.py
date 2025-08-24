import jwt
import logging
from datetime import timedelta, timezone, datetime
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password

SECRET_KEY = settings.SECRET_KEY
logger = logging.getLogger(__name__)


def hash_password(password: str) -> str:
    return make_password(password)


def compare_passwords(password: str, hashed_password: str) -> bool:
    return check_password(password, hashed_password)


def create_access_token(user_id: str, expires_delta: timedelta = timedelta(hours=1)):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.now(timezone.utc) + expires_delta,
        "iat": datetime.now(timezone.utc),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.exceptions.ExpiredSignatureError:
        return None
    except jwt.exceptions.InvalidTokenError:
        return None
    except Exception as e:
        logger.exception("Unexpected error in decode_access_token")
        return None
