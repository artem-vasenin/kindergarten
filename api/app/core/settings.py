from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'ToDo'

    db_host: str = 'localhost'
    db_port: int = 5432
    db_user: str
    db_password: str
    db_name: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
