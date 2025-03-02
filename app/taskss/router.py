
from fastapi import APIRouter,HTTPException, status
from app.taskss.repo import DAO

router = APIRouter(
    prefix="/tasks",
)

exceptiion = HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("")
async def get_all():
    return await DAO.get_all()

@router.get("/{task_id}")
async def get_id(task_id: int):
    res = await DAO.find_by_id(id=task_id)
    if res:
        return res
    else:
        raise exceptiion

@router.post("")
async def add_task(
    title: str,
    description: str,
):
    return await DAO.add(title=title, description=description)

@router.delete("/{task_id}")
async def deleete(task_id: int):
    await DAO.delete_one(id=task_id)

@router.put("/{task_id}")
async def add_change(
    task_id: int,
    title: str,
    description: str,
):
    res = await DAO.update_task(id=task_id, title=title, description=description)
    if res:
        return res
    else:
        raise exceptiion





