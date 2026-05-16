from enum import Enum
from typing import TYPE_CHECKING
from sqlalchemy import String, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from app.cms.templates.models import TemplateFieldModel

class FieldType(str, Enum):
    STR = 'str'
    INT = 'int'
    FLOAT = 'float'
    DATETIME = 'datetime'
    BOOL = 'bool'

    FILES = 'files'
    REPEATER = 'repeater'
    BLOCKS = 'blocks'
    JSON = 'json'

class FieldModel(Base):
    __tablename__ = "fields"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True, default='')
    field_type: Mapped[FieldType] = mapped_column(SQLEnum(FieldType), nullable=False)
    default_value: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    settings: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)

    template_fields: Mapped[list['TemplateFieldModel']] = relationship(back_populates='field')
