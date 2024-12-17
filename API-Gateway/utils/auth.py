from functools import wraps
from fastapi import HTTPException, status

def authenticate(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Logica di autenticazione
        # if not valid_token:
        #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        return await func(*args, **kwargs)
    return wrapper