from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas  ,oauth2
from ..database import get_db


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)



@router.post("/send" , response_model= schemas.PostResponse , status_code=status.HTTP_201_CREATED)
async def posts(post : schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=List[schemas.PostOut])
async def get_posts(db : Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user),
                    limit: int = 10, skip: int = 0, search: Optional[str] = "") :
    # posts = db.query(models.Post).filter(models.Post.content.contains(search)).limit(limit).offset(skip).all()
    # posts = db.query(models.Post).all()
    # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


@router.get("/{id}" , response_model=schemas.PostOut)
async def get_post(id : int, db : Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)) :
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.id == id).first()
    if not post :
        raise HTTPException(status_code=404, detail=f"Post {id} was not found")
    return post


@router.delete("/delete/{id}" , status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id : int, db : Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)) :
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first() :
        raise HTTPException(status_code=404, detail=f"Post {id} was not found")
    if post.first().owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to perform requested action")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/update/{id}" , response_model=schemas.PostResponse)
async def update_post(id : int, post_update : schemas.PostCreate, db : Session = Depends(get_db),
                      current_user: int = Depends(oauth2.get_current_user)) :
    post_query = db.query(models.Post).filter(models.Post.id == id)
    db_post = post_query.first()
    if not db_post :
        raise HTTPException(status_code=404, detail=f"Post {id} was not found")
    if db_post.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to perform requested action")
    post_query.update(post_update.model_dump(exclude_unset=True) , synchronize_session=False)
    db.commit()
    return post_query.first()