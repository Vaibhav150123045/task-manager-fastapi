from sqlalchemy.orm import Session
from models.users import User, UserCredential
from schemas.users import UserCreate
from datetime import datetime
from passlib.hash import bcrypt


def create_new_user(db: Session, user: UserCreate):
    # Create user profile
    new_user = User(
        username=user.username,
        name=user.name,
        DOB=user.DOB,
        email=user.email,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create user credentials
    hashed_pw = bcrypt.hash(user.password)
    new_cred = UserCredential(
        userID=new_user.userID,
        hashed_password=hashed_pw,
        isCurrent=True
    )
    db.add(new_cred)
    db.commit()
    db.refresh(new_cred)

    return new_user
