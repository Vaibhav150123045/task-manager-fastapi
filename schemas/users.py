from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

# Base User schema


class UserBase(BaseModel):
    username: str
    name: Optional[str]
    DOB: Optional[date]
    email: EmailStr

# For creating a new user


class UserCreate(UserBase):
    password: str  # only for signup

# For updating user details


class UserUpdate(BaseModel):
    name: Optional[str]
    DOB: Optional[date]
    email: Optional[EmailStr]

# Response model


class User(UserBase):
    userID: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# =======================
# User Credential schemas
# =======================
class UserCredentialBase(BaseModel):
    userID: int
    hashed_password: str
    isCurrent: bool


class UserCredentialCreate(UserCredentialBase):
    pass


class UserCredential(UserCredentialBase):
    credentialsID: int
    created_at: datetime

    class Config:
        orm_mode = True


# =======================
# User Session schemas
# =======================
class UserSessionBase(BaseModel):
    userID: int
    is_active: bool


class UserSessionCreate(UserSessionBase):
    pass


class UserSession(UserSessionBase):
    sessionID: int
    created_at: datetime

    class Config:
        orm_mode = True
