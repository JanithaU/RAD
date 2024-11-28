from fastapi import HTTPException,status
from core.security import hash_password
from db.models import User


def get_all_users(db):
    users = db.query(User).all()
    return users

def create_user(user,db):
    existing_user = db.query(User).filter(
        (User.username == user.username)
    ).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists",
        )
    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    return new_user