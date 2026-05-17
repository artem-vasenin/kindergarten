import logging
from fastapi import Request
from typing import Annotated
from fastapi import Depends
from sqlalchemy import select

from app.core.settings import Settings
from app.cms.fields.models import FieldModel
from app.core.db import AsyncSession, DbDeps
from app.cms.fields.types import FieldCreateType, FieldUpdateType, FieldType

logger = logging.getLogger(__name__)


class FieldService:
    def __init__(self, db: AsyncSession, settings: Settings):
        self.db = db
        self.settings = settings


    async def get_list(self)->list[FieldType]:
        result = (await self.db.execute(select(FieldModel).order_by(FieldModel.id))).scalars().all()
        return [FieldType.model_validate(i) for i in result]


    async def get_item(self, iid: int)->FieldModel | None:
        return (await self.db.execute(select(FieldModel).where(FieldModel.id == iid))).scalar_one_or_none()


    async def set_item(self, dto: FieldCreateType)->FieldType:
        item = FieldModel(**dto.model_dump(exclude_unset=True))
        self.db.add(item)
        await self.db.commit()
        await self.db.refresh(item)
        return FieldType.model_validate(item)


    async def upd_item(self, iid: int, dto: FieldUpdateType)->FieldType | None:
        item = await self.get_item(iid)
        if not item:
            return None
        values = dto.model_dump(exclude_unset=True)
        for k, v in values.items():
            setattr(item, k, v)
        await self.db.commit()
        await self.db.refresh(item)
        return FieldType.model_validate(item)


    async def del_item(self, iid: int)->bool:
        item = await self.get_item(iid)
        if not item:
            return False
        await self.db.delete(item)
        await self.db.commit()
        return True


def get_service(db: DbDeps, req: Request):
    return FieldService(db=db, settings=req.app.state.settings)


FieldServiceDeps = Annotated[
    FieldService,
    Depends(get_service),
]