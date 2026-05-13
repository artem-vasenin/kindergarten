import logging
from typing import Annotated
from sqlalchemy import select, desc
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, Request

from app.user.models import UserModel
from app.core.settings import Settings
from app.core.db import DbDeps, AsyncSession
from app.user.schemas import UserRegReq, UserUpdReq, UserFull, UserFind
from app.utils.security import hash_password, check_password, add_token, get_uid_by_token


logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

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
            logger.error('<Del User> UID is not found')
            return False
        user = await self.find_user(UserFind(id=uid), no_error=True)
        if not user:
            logger.error('<Del User> User is not found')
            return False
        await self.db.delete(user)
        await self.db.commit()
        return True


    async def get_list(self)->list[UserFull]:
        users = (await self.db.execute(select(UserModel).order_by(desc(UserModel.id)))).scalars()
        return [self.transform_user(i) for i in users]


    async def find_user(self, data: UserFind, no_error: bool = False)->UserModel | None:
        if not data.email and not data.id:
            logger.error("Email and ID not found")
            if no_error:
                return None
            else:
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

async def me(
        token: Annotated[str, Depends(oauth2_scheme)],
        request: Request,
        user_service: UserServiceDeps,
) -> UserModel:
    if not token:
        logger.error("<Me> Token not found")
        raise HTTPException(status_code=404, detail="Permission Denied")
    uid = get_uid_by_token(token, request.app.state.settings.jwt_secret)
    if not uid:
        logger.error("<Me> UID not found")
        raise HTTPException(status_code=404, detail="Permission Denied")
    user = await user_service.find_user(UserFind(id=uid))
    if not user:
        logger.error("<Me> User not found")
        raise HTTPException(status_code=404, detail="Permission Denied")
    return user


MeDeps = Annotated[UserModel, Depends(me)]

async def admin(user: MeDeps):
    if not user or not user.role == 'admin':
        logger.error("<Admin> User not found or role is not admin")
        raise HTTPException(status_code=403, detail="Permission Denied")
    return user

AdminDeps = Annotated[UserModel, Depends(admin)]