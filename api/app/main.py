import logging
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select

from app.core.db import DbDeps
from app.core.settings import Settings
# from app.user.client_routes import router as user_client_router
# from app.user.admin_routes import router as user_admin_router
# from app.task.client_routes import router as task_client_router
# from app.task.admin_routes import router as task_admin_router


logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    settings = Settings() # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app_name,
        openapi_tags=[
            # {'name': 'Client Users', 'description': 'Роуты пользователей для клиентов'},
            # {'name': 'Admin Users', 'description': 'Роуты пользователей для администраторов'},
            # {'name': 'Client Tasks', 'description': 'Роуты задач для клиентов'},
            # {'name': 'Admin Tasks', 'description': 'Роуты задач для администраторов'},
        ]
    )
    client_router = APIRouter(prefix="/api")
    admin_router = APIRouter(prefix="/api/admin")

    # client_router.include_router(user_client_router)
    # client_router.include_router(task_client_router)
    # admin_router.include_router(user_admin_router)
    # admin_router.include_router(task_admin_router)

    new_app.state.settings = settings
    new_app.include_router(client_router)
    new_app.include_router(admin_router)

    new_app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            'http://localhost:5173',
        ],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    logger.info(f"Запускаем сервер: {settings.app_name}")

    return new_app

app = create_app()
@app.get('/')
def test(db: DbDeps):
    # res = db.execute(select(1))
    return {'res': 1}