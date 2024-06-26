from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..db import get_db
from ..models import Post, User, Like
from ..excetions import Exception403, Exception404
from ..schemas import *

from . import oauth2

router = APIRouter(
    prefix='/posts',
    tags=["Posts"]
)

# @router.get("/", response_model=list[PostSchema])
@router.get("/")
def test_posts(db: Session = Depends(get_db),
               current_user: User = Depends(oauth2.get_current_user)):
    posts = db.query(Post, func.count(Like.post_id).label("Amount of likes")).filter(Post.user_id == current_user.id).join(Like, Like.post_id == Post.primary_key, isouter=True).group_by(Post.primary_key).all()
    return {
        "data": [ {"Post": i[0], "Likes": i[1]} for i in posts]
    }

@router.get("/{primary_key}")
def get_post(primary_key: int, db: Session = Depends(get_db)):
    post = db.query(Post).get(primary_key)
    if post == None:
        raise Exception404
    return {
        "data" : post
        }

@router.post("/create", status_code=201, response_model=MessageSchema)
def create_posts(post: PostSchema, db: Session = Depends(get_db),
                 current_user: User = Depends(oauth2.get_current_user)):
    print(current_user.email)
    print(current_user.id)
    new_post = Post(post.model_dump(), current_user.id)
    new_post.user_id = current_user.id
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {
        "message": "successfully added your request!"
        }

@router.put("/update")
def update_post(post: PostSchema, db: Session = Depends(get_db),
                current_user: User = Depends(oauth2.get_current_user)):
    ind = post.model_dump().get("primary_key")
    if ind == None :
        raise Exception403
    post2 = db.query(Post).get(ind)
    if post2 == None:
        raise Exception404
    if post2.user_id != current_user.id:
        raise Exception403
    post2.update(post.model_dump())
    return {
        "message": "successfully updated!"
        }

@router.delete("/delete")
def delete_post(payload: dict, db: Session = Depends(get_db),
                current_user: User = Depends(oauth2.get_current_user)):
    ind = payload.get("primary_key")
    if ind == None:
        raise Exception403
    post_to_delete = db.query(Post).get(ind)

    if post_to_delete == None:
        raise Exception404
    
    if post_to_delete.user_id != current_user.id:
        raise Exception403

    db.query(Post).delete()
    return {
        "message": "successfully deleted!"
        }

@router.post("/like")
def like_post(payload: LikeSchema, db: Session = Depends(get_db),
              current_user: User = Depends(oauth2.get_current_user)):
    if db.query(Post).get(payload.post_id) == None:
        raise Exception404
    like = db.query(Like).filter(Like.user_id == current_user.id, Like.post_id == payload.post_id)
    if like.count() != 0:
        db.query(Like).delete()
        db.commit()
        return {
            "message": "unliked!"
            }
    new_like = Like(user_id=current_user.id, post_id=payload.post_id)
    db.add(new_like)
    db.commit()
    return {
        "message": "liked!"
        }
