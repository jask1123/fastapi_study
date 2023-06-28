from typing import List

from fastapi import APIRouter

import api.schemas.posts as post_schema

router = APIRouter()


@router.get("/posts", response_model=List[post_schema.Post])
async def list_posts():
    return [post_schema.Post(id=1, text='水を買ったよ')]  # type: ignore

@router.post("/posts")
async def create_post():
    pass

@router.put("/posts/{id}")
async def update_post():
    pass

@router.delete("/posts/{id}")
async def delete_post():
    pass