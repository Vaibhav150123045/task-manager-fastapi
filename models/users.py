from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base  # Import your SQLAlchemy Base here


# =======================
# User Table
# =======================
class User(Base):
    __tablename__ = "User"

    userID = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String)
    DOB = Column(Date)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    credentials = relationship("UserCredential", back_populates="user")
    sessions = relationship("UserSession", back_populates="user")


# =======================
# User Credential Table
# =======================
class UserCredential(Base):
    __tablename__ = "UserCredentialDetails"

    credentialsID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("User.userID"))
    hashed_password = Column(String, nullable=False)
    isCurrent = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="credentials")


# =======================
# User Session Table
# =======================
class UserSession(Base):
    __tablename__ = "UserSessions"

    sessionID = Column(Integer, primary_key=True, index=True)
    userID = Column(Integer, ForeignKey("User.userID"))
    created_at = Column(DateTime, default=func.now())
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="sessions")
