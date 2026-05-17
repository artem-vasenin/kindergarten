from fastapi import APIRouter

from app.cms.fields.services import FieldServiceDeps
from app.cms.fields.types import FieldCreateType, FieldUpdateType, FieldType


router = APIRouter(prefix='/fields', tags=['Field'])

@router.get('/', response_model=list[FieldType], summary='Fields list')
async def get_list(srv: FieldServiceDeps)->list[FieldType]:
    return await srv.get_list()

@router.get('/{iid}', response_model=FieldType, summary='Fields detail')
async def get_item(srv: FieldServiceDeps, iid: int)->FieldType:
    return await srv.get_item(iid)

@router.post('/', status_code=201, response_model=FieldType, summary='Fields create')
async def set_item(srv: FieldServiceDeps, dto: FieldCreateType)->FieldType:
    return await srv.set_item(dto)

@router.patch('/{iid}', status_code=200, response_model=FieldType, summary='Fields update')
async def upd_item(srv: FieldServiceDeps, iid: int, dto: FieldUpdateType)->FieldType:
    return await srv.upd_item(iid, dto)

@router.delete('/{iid}', status_code=200, response_model=bool, summary='Fields delete')
async def del_item(srv: FieldServiceDeps, iid: int)->bool:
    return await srv.del_item(iid)