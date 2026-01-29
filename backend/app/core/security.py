from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import CONNECTOR_TOKEN

security = HTTPBearer(auto_error=True)

def validate_connector_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> str:
    token = credentials.credentials
    
    if token != CONNECTOR_TOKEN:
        raise HTTPException(
            status_code=403,
            detail="Invalid connector token",
        )

    return token

