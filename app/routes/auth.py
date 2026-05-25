from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models, oauth2, utils, schemas
from ..database import get_db


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@router.post("/", response_model=schemas.Token)
def login_user(
    user_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.email == user_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials!"
        )

    if not utils.verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials!"
        )

    access_token = oauth2.create_access_token(
        data={"user_id": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }