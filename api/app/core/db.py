from typing import Annotated
from sqlalchemy import select
from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.settings import Settings
import app.cms.models


settings = Settings() # type: ignore[call-arg]
engine = create_async_engine(settings.database_url, echo=True)
async_session_factory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session_factory() as session:
        yield session

async def test_db(session: AsyncSession):
    res = await session.execute(select(1))
    return res.scalar_one()

DbDeps = Annotated[
    AsyncSession,
    Depends(get_db),
]