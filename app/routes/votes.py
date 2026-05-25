from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, oauth2


router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote_details: schemas.Vote,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    post = db.query(models.Post).filter(
        models.Post.id == vote_details.post_id
    ).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {vote_details.post_id} does not exist!"
        )

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote_details.post_id,
        models.Vote.user_id == current_user.id
    )

    found_vote = vote_query.first()

    if vote_details.dir == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"User with id: {current_user.id} has already voted "
                    f"for post with id: {vote_details.post_id}!"
                )
            )

        new_vote = models.Vote(
            post_id=vote_details.post_id,
            user_id=current_user.id
        )

        db.add(new_vote)
        db.commit()

        return {"message": "Successfully added vote!"}

    if not found_vote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vote for post with id: {vote_details.post_id} does not exist!"
        )

    vote_query.delete(synchronize_session=False)
    db.commit()

    return {"message": "Successfully deleted vote!"}


@router.get("/")
def get_all_votes(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user)
):
    votes = db.query(models.Vote).all()
    return votes

    
    
    

