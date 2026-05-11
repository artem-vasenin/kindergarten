from sqlalchemy import String
from typing import Any, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from app.task.models import TaskModel

class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(1024), nullable=False)
    role: Mapped[str] = mapped_column(String(128), nullable=False, default='guest')
    tasks: Mapped[list["TaskModel"]] = relationship(
        "TaskModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __init__(self, email: str, password: str, role: str = 'guest', **kw: Any) -> None:
        super().__init__(**kw)
        self.email = email
        self.password = password
        self.role = role