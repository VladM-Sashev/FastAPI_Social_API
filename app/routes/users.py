from fastapi import HTTPException, status, Depends, APIRouter, Response
from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas, models, utils


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOut
)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered!"
        )

    new_user = models.User(
        email=user.email,
        password=utils.password_hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/", response_model=list[schemas.UserOut])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.get("/{id}", response_model=schemas.UserOut)
def get_one_user(
    id: int,
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist!"
        )

    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_user(
    id: int,
    db: Session = Depends(get_db)
):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist!"
        )

    user_query.delete(synchronize_session=False)
    db.commit()