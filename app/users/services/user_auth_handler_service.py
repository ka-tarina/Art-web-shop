"""Module for User Authentification Handler service."""
import time
from typing import Dict
import jwt
from app.config import settings
from app.users.enums import UserRole

USER_SECRET = settings.USER_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def signJWT(user_id: str, role: UserRole) -> Dict[str, str]:
    """Makes JWT payload and returns a token"""
    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + 1200
    }

    token = jwt.encode(payload, USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeJWT(token: str) -> Dict or None:
    """Decodes JWT token"""
    try:
        decoded_token = jwt.decode(token, USER_SECRET, algorithms=[JWT_ALGORITHM])
        user_id: str = decoded_token.get("user_id")
        role: UserRole = decoded_token.get("role")
        if user_id is None or role is None:
            return None
        return {"user_id": user_id, "role": role}
    except jwt.exceptions.ExpiredSignatureError:
        return None
