from http.client import HTTPException

from fastapi import APIRouter, Depends

import api.schemas.done as done_schema
import api.cruds.done as done_crud
from api.db import get_db

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.put('/done/{task_id}/done', response_model=done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db=Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await done_crud.create_done(db, task_id=task_id)


@router.delete('/done/{task_id}/done', response_model=None)
async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await done_crud.delete_done(db, original=done)
