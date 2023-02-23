"""Model for JWT Bearer controller"""
import time
from typing import List
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWTError
from app.users.enums import UserRole
from app.users.services import decodeJWT


class JWTBearer(HTTPBearer):
    """Class to authenticate JWT tokens."""
    def __init__(self, roles: List[UserRole] = None, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.roles = roles

    async def __call__(self, request: Request):
        """Method to call the bearer token authentication."""
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            try:
                payload = decodeJWT(credentials.credentials)

                if self.roles is not None and UserRole(payload.get("role")) != self.roles:
                    raise HTTPException(
                        status_code=403, detail="Not enough permissions."
                    )
                if time.time() > payload.get("expires"):
                    raise HTTPException(status_code=401, detail="Token has expired.")

                return credentials.credentials

            except PyJWTError as e:
                raise HTTPException(status_code=401, detail=str(e))

        else:
            raise HTTPException(status_code=401, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> dict:
        """Verifies if jwt token is valid."""
        is_token_valid: bool = False
        try:
            payload = decodeJWT(jwtoken)
        except Exception as e:
            print(e)
            payload = None
        if payload:
            is_token_valid = True
        return {"valid": is_token_valid, "role": payload["role"]}
