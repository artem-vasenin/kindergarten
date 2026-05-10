import logging
from fastapi import FastAPI, Request

from app.core.db import DbDeps, test_db
from app.core.settings import Settings


logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    settings = Settings() # type: ignore[call-arg]
    new_app = FastAPI(title=settings.app_name,)
    new_app.state.settings = settings

    logger.info(f"Запускаем список дел: {settings.app_name}")

    return new_app

app = create_app()
@app.get("/")
async def read_root(request: Request, db: DbDeps):
    res = await test_db(db)
    print(request.app.state.settings, res)
    return {"Hello": "World"}