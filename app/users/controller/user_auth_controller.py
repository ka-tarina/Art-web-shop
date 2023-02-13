import time
from typing import Dict

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config import settings
from app.users.services import decodeJWT

# class JWTSuperUserBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super(JWTSuperUserBearer, self).__init__(auto_error=auto_error)
#
#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTSuperUserBearer, self).__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
#             if not self.verify_jwt(credentials.credentials):
#                 raise HTTPException(status_code=403, detail="Invalid token or expired token.")
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")
#
#     def verify_jwt(self, jwtoken: str) -> bool:
#         is_token_valid: bool = False
#         try:
#             payload = decodeSuperUserJWT(jwtoken)
#         except:
#             payload = None
#         if payload:
#             is_token_valid = True
#         return is_token_valid
#
# class JWTClassicUserBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super(JWTClassicUserBearer, self).__init__(auto_error=auto_error)
#
#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTClassicUserBearer, self).__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
#             if not self.verify_jwt(credentials.credentials):
#                 raise HTTPException(status_code=403, detail="Invalid token or expired token.")
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")
#
#     def verify_jwt(self, jwtoken: str) -> bool:
#         is_token_valid: bool = False
#         try:
#             payload = decodeClassicUserJWT(jwtoken)
#         except:
#             payload = None
#         if payload:
#             is_token_valid = True
#         return is_token_valid


class JWTBearer(HTTPBearer):
    def __init__(self, role: str, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload.get("valid"):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            if payload.get("role") != self.role:
                raise HTTPException(
                    status_code=403,
                    detail="User with provided role is not permitted to access this " "route.",
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> dict:
        is_token_valid: bool = False
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return {"valid": is_token_valid, "role": payload["role"]}
