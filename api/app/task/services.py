import logging
from typing import Annotated
from sqlalchemy import select, desc
from fastapi import Request, Depends, HTTPException

from app.task.models import TaskModel
from app.core.settings import Settings
from app.core.db import AsyncSession, DbDeps
from app.task.schemas import TaskFull, TaskCreateReq, TaskUpdReq


logger = logging.getLogger(__name__)

class TaskService:
    def __init__(self, db: AsyncSession, settings: Settings):
        self.db = db
        self.settings = settings


    async def get_list(self, uid: int | None = None, is_admin: bool = False)->list[TaskFull]:
        q = select(TaskModel)
        if not is_admin:
            q = q.where(TaskModel.user_id == uid)
        q.order_by(desc(TaskModel.id))
        result = (await self.db.execute(q)).scalars().all()
        return [self.transform_item(i) for i in result]


    async def get_item(
            self,
            tid: int,
            uid: int | None = None,
            no_error: bool = False,
            is_admin: bool = False,
    )->TaskModel | None:
        if not is_admin:
            if not uid:
                logger.error('<Get Task> UID not provided')
                raise HTTPException(status_code=404, detail="User not found")
            q = select(TaskModel).where(TaskModel.user_id == uid, TaskModel.id == tid)
        else:
            q = select(TaskModel).where(TaskModel.id == tid)
        item = (await self.db.execute(q)).scalar_one_or_none()
        if not no_error and not item:
            logger.error('<Get Task> Task not found')
            raise HTTPException(status_code=404, detail="Task not found")

        return item


    async def set_item(self, uid: int, data: TaskCreateReq)->TaskFull:
        item = TaskModel(**data.model_dump(), user_id=uid)
        self.db.add(item)
        await self.db.commit()
        await self.db.refresh(item)
        return self.transform_item(item)


    async def update_item(
            self,
            tid: int,
            data: TaskUpdReq,
            uid: int | None = None,
            is_admin: bool = False,
    )->TaskFull:
        item = await self.get_item(tid=tid, uid=uid, is_admin=is_admin, no_error=True)
        if not item:
            logger.error('<Upd Task> Task not found')
            raise HTTPException(status_code=404, detail="Task not found")
        patch = data.model_dump(exclude_unset=True)
        for f, v in patch.items():
            setattr(item, f, v)
        await self.db.commit()
        await self.db.refresh(item)
        return self.transform_item(item)


    async def del_item(self, tid: int, uid: int | None = None, is_admin: bool = False)->bool:
        item = await self.get_item(uid=uid, tid=tid, is_admin=is_admin, no_error=True)
        if not item:
            logger.error('<Del Task> Task not found')
            raise HTTPException(status_code=404, detail="Task not found")
        await self.db.delete(item)
        await self.db.commit()
        return True


    def transform_item(self, item: TaskModel)->TaskFull:
        return TaskFull(
            id=item.id,
            name=item.name,
            user_id=item.user_id,
            description=item.description,
            checked=item.checked
        )


def get_service(db: DbDeps, req: Request)->TaskService:
    return TaskService(db=db, settings=req.app.state.settings)


TaskServiceDeps = Annotated[
    TaskService,
    Depends(get_service),
]