from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

class UserCreate(BaseModel):
    email : EmailStr
    password : str
    model_config = {
        "from_attributes": True
    }

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at: datetime
    model_config = {
        "from_attributes": True
    }

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    model_config = {
        "from_attributes": True
    }

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True



class PostCreate(PostBase):
    pass

# class PostResponse(BaseModel):
#     id : int
#     title: str
#     content: str
#     published: bool
#     created_at: datetime
#
#     class Config:
#     from_attributes = True

class PostResponse(PostBase):
    id : int
    created_at: datetime
    owner_id : int
    owner : UserOut

    model_config = {
        "from_attributes": True
    }


# from typing import Literal

class Vote(BaseModel):
    post_id: int
    # dir: conint(le=1)
    # dir: Literal[0, 1]
    dir: conint(ge=0, le=1)


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    model_config = {"from_attributes": True}