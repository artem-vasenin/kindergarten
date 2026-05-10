from typing import Any
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(1024), nullable=False)
    role: Mapped[str] = mapped_column(String(128), nullable=False, default='guest')

    def __init__(self, email: str, password: str, role: str, **kw: Any) -> None:
        super().__init__(**kw)
        self.email = email
        self.password = password
        self.role = role