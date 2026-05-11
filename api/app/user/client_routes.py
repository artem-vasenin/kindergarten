from fastapi import APIRouter

from app.user.services import UserServiceDeps, AdminDeps, MeDeps
from app.user.schemas import UserRegReq, UserFull, UserUpdReq, UserFind


router = APIRouter(prefix='/user', tags=['Client Users'])

@router.post('/login', status_code=200, response_model=str | None)
async def login(service: UserServiceDeps, data: UserRegReq)->str | None:
    return await service.login(data)

@router.post('/register', status_code=201, response_model=str)
async def register(service: UserServiceDeps, data: UserRegReq)->str:
    return await service.register(data)



