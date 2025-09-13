import uuid
from sqlalchemy.orm import Session
from models.users import User, UserCredential
from schemas.users import UserCreate, UserSession
from datetime import datetime, timedelta
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


def create_user_session(db: Session, user_id: int, session_duration_minutes: int = 60):
    """
    Creates a new user session for the given user_id.

    Args:
        db (Session): SQLAlchemy database session.
        user_id (int): The ID of the user for whom to create the session.
        session_duration_minutes (int): How long the session should last (default: 60 mins).

    Returns:
        UserSession: The newly created user session object.
    """

    # Generate a unique session token
    session_token = str(uuid.uuid4())
    expires_at = datetime.now() + timedelta(minutes=session_duration_minutes)

    # Create the new session record
    new_session = UserSession(
        userID=user_id,
        session_token=session_token,
        created_at=datetime.now(),
        expires_at=expires_at,
        is_active=True
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return new_session
