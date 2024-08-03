from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_token_header(token: str = Depends(oauth2_scheme)):
    if token != "mariah-carey":
        raise HTTPException(status_code=400, detail="Invalid token")