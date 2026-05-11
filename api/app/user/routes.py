from fastapi import APIRouter

from app.user.schemas import UserRegReq, UserFull, UserUpdReq, UserFind
from app.user.services import UserServiceDeps


router = APIRouter(prefix='/user', tags=['Users'])

@router.post('/login', status_code=200, response_model=str | None)
async def login(service: UserServiceDeps, data: UserRegReq)->str | None:
    return await service.login(data)

@router.post('/register', status_code=201, response_model=str)
async def register(service: UserServiceDeps, data: UserRegReq)->str:
    return await service.register(data)

@router.get('/', response_model=list[UserFull])
async def get_list(service: UserServiceDeps)->list[UserFull]:
    return await service.get_list()

@router.get('/{uid}', response_model=UserFull | None)
async def get_by_id(service: UserServiceDeps, uid:int)->UserFull | None:
    payload = UserFind(id=uid)
    user = await service.find_user(payload)
    return service.transform_user(user)

@router.get('/get_by_email/{email}', response_model=UserFull | None)
async def get_by_email(service: UserServiceDeps, email:str)->UserFull | None:
    payload = UserFind(email=email)
    user = await service.find_user(payload)
    return service.transform_user(user)

@router.patch('/{uid}', status_code=201, response_model=UserFull | None)
async def update(service: UserServiceDeps, uid:int, data:UserUpdReq)->UserFull | None:
    return await service.update(uid, data)

@router.delete('/{uid}', status_code=200, response_model=bool)
async def delete(service: UserServiceDeps, uid:int)->bool:
    return await service.delete(uid)



