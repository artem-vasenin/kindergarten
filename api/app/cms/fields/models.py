from typing import TYPE_CHECKING, Any
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base import Base

if TYPE_CHECKING:
    from app.cms.templates.models import TemplateFieldModel


class FieldModel(Base):
    __tablename__ = "fields"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True, default='')
    field_type: Mapped[str] = mapped_column(String(32), nullable=False)
    default_value: Mapped[Any | None] = mapped_column(JSONB, nullable=True)
    settings: Mapped[Any] = mapped_column(JSONB, nullable=False, default=dict)

    template_fields: Mapped[list['TemplateFieldModel']] = relationship('TemplateFieldModel', back_populates='field')
