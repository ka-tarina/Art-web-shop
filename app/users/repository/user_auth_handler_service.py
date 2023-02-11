import jwt
import time
from typing import Dict
from app.config import settings

JWT_SUPER_USER_SECRET = settings.SUPER_USER_SECRET
JWT_CLASSIC_USER_SECRET = settings.CLASSIC_USER_SECRET
USER_SECRET = settings.USER_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def signSuperUserJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "is_super_user": "super_user",
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, JWT_SUPER_USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeSuperUserJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SUPER_USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


def signClassicUserJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "is_super_user": "user",
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, JWT_CLASSIC_USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeClassicUserJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_CLASSIC_USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


def signJWT(user_id: str, role:str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + 1200
    }

    token = jwt.encode(payload, USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
