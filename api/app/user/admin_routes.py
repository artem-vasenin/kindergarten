from fastapi import APIRouter

from app.user.services import UserServiceDeps, AdminDeps, MeDeps
from app.user.schemas import UserRegReq, UserFull, UserUpdReq, UserFind


router = APIRouter(prefix='/user', tags=['Admin Users'])

@router.post('/register', status_code=201, response_model=str)
async def register(service: UserServiceDeps, data: UserRegReq)->str:
    return await service.register(data)

@router.get('/', response_model=list[UserFull])
async def get_list(service: UserServiceDeps, me: MeDeps)->list[UserFull]:
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
async def update(service: UserServiceDeps, uid:int, data:UserUpdReq, admin: AdminDeps)->UserFull | None:
    return await service.update(uid, data)

@router.delete('/{uid}', status_code=200, response_model=bool)
async def delete(service: UserServiceDeps, uid:int, admin: AdminDeps)->bool:
    return await service.delete(uid)



