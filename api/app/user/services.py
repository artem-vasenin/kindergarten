import logging
from typing import Annotated
from fastapi import Depends, HTTPException, Request
from sqlalchemy import select

from app.user.models import UserModel
from app.core.settings import Settings
from app.core.db import DbDeps, AsyncSession
from app.utils.security import hash_password, check_password, add_token
from app.user.schemas import UserRegReq, UserUpdReq, UserFull, UserFind

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, db: AsyncSession, settings: Settings):
        self.db = db
        self.settings = settings


    async def login(self, data: UserRegReq)-> str | None:
        user = (await self.db.execute(select(UserModel).where(UserModel.email == data.email))).scalar_one_or_none()
        if not user:
            logger.error("User not found")
            raise HTTPException(status_code=400, detail="User not found")
        if not check_password(data.password, user.password):
            logger.error("User not found")
            raise HTTPException(status_code=400, detail="User not found")
        return add_token(uid=user.id, secret=self.settings.jwt_secret, time=self.settings.jwt_time)


    async def register(self, data: UserRegReq)->str:
        payload = UserFind(email=data.email)
        double_item = await self.find_user(payload, no_error=True)
        if double_item:
            logger.error(f"{data.email} already registered")
            raise HTTPException(status_code=400, detail="Email already registered")

        try:
            hashed_password = hash_password(data.password)
        except:
            logger.error('Invalid password')
            raise HTTPException(status_code=400, detail="Invalid password")

        user = UserModel(email=data.email, password=hashed_password)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return add_token(user.id, self.settings.jwt_secret, self.settings.jwt_time)


    async def update(self, uid: int, data: UserUpdReq)->UserFull | None:
        user = await self.find_user(UserFind(id=uid))
        if not data.password and not data.role:
            logger.error("Data is empty")
            raise HTTPException(status_code=400, detail="Data is empty")
        if data.password:
            hashed_password = hash_password(data.password)
            user.password = hashed_password
        if data.role and (data.role == 'admin' or data.role == 'guest'):
            user.role = data.role
        await self.db.commit()
        await self.db.refresh(user)

        return self.transform_user(user) if user else None


    async def delete(self, uid: int)->bool:
        if not uid:
            return False
        user = await self.find_user(UserFind(id=uid), no_error=True)
        if not user:
            return False
        await self.db.delete(user)
        await self.db.commit()
        return True


    async def get_list(self)->list[UserFull]:
        users = (await self.db.execute(select(UserModel))).scalars()
        return [self.transform_user(i) for i in users]


    async def find_user(self, data: UserFind, no_error: bool = False)->UserModel | None:
        if not data.email and not data.id:
            if no_error:
                return None
            else:
                logger.error("Email and ID not found")
                raise HTTPException(status_code=400, detail="Email and ID not found")

        q = select(UserModel)
        if data.email:
            q = q.where(UserModel.email == data.email)
        if data.id:
            q = q.where(UserModel.id == data.id)
        user = (await self.db.execute(q)).scalar_one_or_none()

        if not no_error:
            if not user:
                logger.error("User not found")
                raise HTTPException(status_code=404, detail="User not found")
        return user


    def transform_user(self, user: UserModel | None)->UserFull | None:
        return UserFull(id=user.id, email=user.email, role=user.role) if user else None


def get_service(db: DbDeps, req: Request)->UserService:
    return UserService(db, req.app.state.settings)


UserServiceDeps = Annotated[
    UserService,
    Depends(get_service),
]