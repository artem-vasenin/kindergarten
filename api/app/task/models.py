from typing import Any, TYPE_CHECKING
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from app.user.models import UserModel


class TaskModel(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True, default='')
    checked: Mapped[bool] = mapped_column(Boolean(), nullable=True, default=False)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    user: Mapped['UserModel'] = relationship("UserModel", back_populates="tasks")

    def __init__(
            self,
            name: str,
            user_id: int,
            description: str = '',
            checked: bool = False,
            **kw: Any,
    ) -> None:
        super().__init__(**kw)
        self.name = name
        self.user_id = user_id
        self.description = description
        self.checked = checked