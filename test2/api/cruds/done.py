from typing import Optional, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model


def get_done(db: Session, task_id: int) -> task_model.Done | None:
    result: Result = db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    done: Optional[Tuple[task_model.Done]] = result.first()
    return done[0] if done is not None else None


def create_done(db: Session, task_id: int) -> task_model.Done:
    done = task_model.Done(id=task_id)
    db.add(done)
    db.commit()
    db.refresh(done)
    return done


def delete_done(db: Session, original: task_model.Done) -> None:
    db.delete(original)
    db.commit()
