from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.users import UserCreate
from database_crud.users import create_new_user

router = APIRouter()


# | `create_new_user`          | Sign up → Add user details & credentials


@router.post("/signup", response_model=UserCreate)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(db, user)


# | `update_user_password`     | Change Password → Add new credentials record      |
# | `create_new_session`       | Sign in → Verify credentials, generate JWT token  |
# | `update_session`           | Logout → Mark session inactive                   |
# | `update_user_details`      | Update profile data → Modify user table fields    |
