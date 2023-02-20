import time
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import PyJWTError
from app.users.enums import UserRole
from app.users.services import UserAuthHandlerServices


class JWTBearer(HTTPBearer):
    def __init__(self, role: UserRole = None, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            try:
                payload = UserAuthHandlerServices.decodeJWT(credentials.credentials)

                if self.role is not None and UserRole(payload.get("role")) != self.role:
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
        is_token_valid: bool = False
        try:
            payload = UserAuthHandlerServices.decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return {"valid": is_token_valid, "role": payload["role"]}
