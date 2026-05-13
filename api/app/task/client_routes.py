from fastapi import APIRouter

from app.user.services import MeDeps
from app.task.services import TaskServiceDeps
from app.task.schemas import TaskFull, TaskCreateReq, TaskUpdReq


router = APIRouter(prefix='/task', tags=['Client Tasks'])

@router.get(
    '/',
    status_code=200,
    response_model=list[TaskFull],
    summary='Получение списка своих задач',
)
async def get_list(service: TaskServiceDeps, me: MeDeps)->list[TaskFull]:
    return await service.get_list(me.id)


@router.get(
    '/{tid}',
    status_code=200,
    response_model=TaskFull | None,
    summary='Получение задачи по ее ID',
)
async def get_item(service: TaskServiceDeps, tid: int, me: MeDeps)->TaskFull | None:
    result = await service.get_item(uid=me.id, tid=tid)
    return service.transform_item(result) if result else None


@router.post(
    '/',
    status_code=201,
    response_model=TaskFull,
    summary='Добавление задачи',
)
async def set_item(service: TaskServiceDeps, data: TaskCreateReq, me: MeDeps)->TaskFull:
    data.user_id = me.id
    return await service.set_item(data=data)


@router.patch(
    '/{tid}',
    status_code=201,
    response_model=TaskFull | None,
    summary='Изменение данных выбранной задачи',
)
async def upd_item(service: TaskServiceDeps, tid: int, data: TaskUpdReq, me: MeDeps)->TaskFull | None:
    return await service.update_item(uid=me.id, tid=tid, data=data)


@router.delete(
    '/{tid}',
    status_code=200,
    response_model=bool,
    summary='Удаление выбранной задачи',
)
async def del_item(service: TaskServiceDeps, tid: int, me: MeDeps)->bool:
    return await service.del_item(uid=me.id, tid=tid)



