from fastapi import APIRouter

from app.task.services import TaskServiceDeps
from app.task.schemas import TaskFull, TaskCreateReq, TaskUpdReq
from app.user.services import AdminDeps


router = APIRouter(prefix='/task', tags=['Admin Tasks'])

@router.get(
    '/',
    status_code=200,
    response_model=list[TaskFull],
    summary='Получение списка задач всех пользователей',
)
async def get_list(service: TaskServiceDeps, admin: AdminDeps)->list[TaskFull]:
    return await service.get_list(is_admin=True)


@router.get(
    '/{tid}',
    status_code=200,
    response_model=TaskFull | None,
    summary='Получение задачи по ее ID',
)
async def get_item(service: TaskServiceDeps, tid: int, admin: AdminDeps)->TaskFull | None:
    result = await service.get_item(tid=tid, is_admin=True)
    return service.transform_item(result) if result else None


@router.post(
    '/',
    status_code=201,
    response_model=TaskFull,
    summary='Добавление задачи',
)
async def set_item(service: TaskServiceDeps, data: TaskCreateReq, admin: AdminDeps)->TaskFull:
    data.user_id = data.user_id if data.user_id else admin.id
    return await service.set_item(data=data)


@router.patch(
    '/{tid}',
    status_code=201,
    response_model=TaskFull | None,
    summary='Изменение данных выбранной задачи',
)
async def upd_item(service: TaskServiceDeps, tid: int, data: TaskUpdReq, admin: AdminDeps)->TaskFull | None:
    return await service.update_item(tid=tid, data=data, is_admin=True)


@router.delete(
    '/{tid}',
    status_code=200,
    response_model=bool,
    summary='Удаление выбранной задачи',
)
async def del_item(service: TaskServiceDeps, tid: int, admin: AdminDeps)->bool:
    return await service.del_item(tid=tid, is_admin=True)



