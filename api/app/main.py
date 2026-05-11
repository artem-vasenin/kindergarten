import logging
from fastapi import FastAPI, Request, APIRouter

from app.core.db import DbDeps, test_db
from app.core.settings import Settings
from app.user.client_routes import router as user_client_router
from app.user.admin_routes import router as user_admin_router


logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    settings = Settings() # type: ignore[call-arg]
    new_app = FastAPI(
        title=settings.app_name,
        openapi_tags=[
            {'name': 'Tasks', 'description': 'Задачи'},
            {'name': 'Client', 'description': 'Роуты для пользователей'},
            {'name': 'Admin', 'description': 'роуты для администраторов'},
        ]
    )
    client_router = APIRouter(prefix="/api", tags=["Client"])
    admin_router = APIRouter(prefix="/api/admin", tags=["Admin"])

    client_router.include_router(user_client_router)
    admin_router.include_router(user_admin_router)

    new_app.state.settings = settings
    new_app.include_router(client_router)
    new_app.include_router(admin_router)

    logger.info(f"Запускаем список дел: {settings.app_name}")

    return new_app

app = create_app()
@app.get("/")
async def read_root(request: Request, db: DbDeps):
    res = await test_db(db)
    print(request.app.state.settings, res)
    return {"Hello": "World"}