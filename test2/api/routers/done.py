from fastapi import APIRouter

router = APIRouter()

@router.put('/done/{task_id}/done',response_model=None)
async def mark_task_as_done(task_id: int):
    return

@router.delete('/done/{task_id}/done',response_model=None)
async def unmark_task_as_done(task_id: int):
    return