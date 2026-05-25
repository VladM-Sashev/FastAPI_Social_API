from fastapi import HTTPException, status, APIRouter, Depends, Response
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from ..database import get_db
from .. import schemas, models, oauth2


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PostOut
)
def create_post(
    post_details: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    new_post = models.Post(
        owner_id=current_user.id,
        **post_details.model_dump()
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/", response_model=list[schemas.PostOutWithVotes])
def get_all_posts(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
    search: Optional[str] = "",
    skip: int = 0,
    limit: int = 10
):
    posts = db.query(
        models.Post,
        func.count(models.Vote.post_id).label("votes")
    ).join(
        models.Vote,
        models.Vote.post_id == models.Post.id,
        isouter=True
    ).group_by(
        models.Post.id
    ).filter(
        models.Post.title.contains(search)
    ).offset(skip).limit(limit).all()

    return posts


@router.get("/{id}", response_model=schemas.PostOut)
def get_one_post(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist!"
        )

    return post


@router.put("/{id}", response_model=schemas.PostOut)
def update_one_post(
    id: int,
    post_info: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist!"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorised action performed!"
        )

    post_query.update(
        post_info.model_dump(),
        synchronize_session=False
    )

    db.commit()

    return post_query.first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_post(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist!"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorised action performed!"
        )

    post_query.delete(synchronize_session=False)
    db.commit()