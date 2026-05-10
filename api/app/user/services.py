from typing import Annotated
from fastapi import Depends

from app.user.schemas import UserRegReq, UserUpdReq, UserFull


class UserService:
    async def login(self, data: UserRegReq)-> str | None:
        print(data)
        return 'token'

    async def register(self, data: UserRegReq)->str:
        return 'token'

    async def update(self, uid: int, data: UserUpdReq)->UserFull | None:
        return None

    async def delete(self, uid: int)->bool:
        return True

    async def get_list(self)->list[UserFull]:
        return []

    async def get_by_id(self, uid: int)->UserFull | None:
        return None

    async def get_by_email(self, email: str)->UserFull | None:
        return None

def get_service():
    return UserService()

UserServiceDeps = Annotated[
    UserService,
    Depends(get_service),
]