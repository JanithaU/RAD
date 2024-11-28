from fastapi import HTTPException, status, Depends
from core.security import decode_access_token
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from sqlalchemy.orm import Session
from db.session import get_db
from db.models import User
import contextvars


current_user_var = contextvars.ContextVar("current_user",default=None)

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


# Dependency to retrieve the current user from the token
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            current_user_var.set(None)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except InvalidTokenError:
        current_user_var.set(None)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = db.query(User).filter(User.username == username).first()
    
    # print(user.id)
    if user is None:
        current_user_var.set(None)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    current_user_var.set(user.id)
    return user


# Custom dependency to check the user's role
def admin_only(user: User = Depends(get_current_user)):
    current_user_var.set("Userdddd")
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return user




