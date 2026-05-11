from fastapi import APIRouter

from app.user.services import UserServiceDeps, MeDeps
from app.user.schemas import UserRegReq, UserFull, UserFind

router = APIRouter(prefix='/user', tags=['Client Users'])

@router.post(
    '/login',
    status_code=200,
    response_model=str | None,
    summary='Вход и получение токена',
)
async def login(service: UserServiceDeps, data: UserRegReq)->str | None:
    return await service.login(data)


@router.post(
    '/register',
    status_code=201,
    response_model=str,
    summary='Регистрация пользователя и получение токена',
)
async def register(service: UserServiceDeps, data: UserRegReq)->str:
    return await service.register(data)


@router.get(
    '/{uid}',
    response_model=UserFull | None,
    summary='Получить пользователя по его ID',
)
async def get_by_id(service: UserServiceDeps, uid:int, me: MeDeps)->UserFull | None:
    payload = UserFind(id=uid)
    user = await service.find_user(payload)
    return service.transform_user(user)
