from sqlalchemy import select
from sqlalchemy.engine import Result
import api.models.task as task_model
import api.schemas.task as task_schema
from typing import List, Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession


async def create_task(db: AsyncSession, task_create: task_schema.TaskCreate, user_id: int) -> task_model.Task:
    task = task_model.Task(**task_create.dict(), user_id=user_id)
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks_with_done(db: AsyncSession,user_id: int) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).select_from(task_model.Task).outerjoin(task_model.Done).where(task_model.Task.user_id == user_id)
        )
    )
    return result.all()


async def get_task(db: AsyncSession, task_id: int) -> task_model.Task | None:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None


async def update_task(db: AsyncSession, task_create: task_schema.TaskCreate,
                      original: task_model.Task) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()
