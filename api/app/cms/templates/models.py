from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, Boolean, UniqueConstraint

from app.core.db import Base


if TYPE_CHECKING:
    from app.cms.fields.models import FieldModel
    from app.cms.pages.models import PageModel

class TemplateModel(Base):
    __tablename__ = "templates"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True, default='')

    fields: Mapped[list['TemplateFieldModel']] = relationship(back_populates='template', cascade='all, delete-orphan')
    entries: Mapped[list['PageModel']] = relationship(back_populates='template', cascade='all, delete-orphan')


class TemplateFieldModel(Base):
    __tablename__ = 'template_fields'

    __table_args__ = (UniqueConstraint('template_id', 'field_id', 'id'),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    template_id: Mapped[int] = mapped_column(ForeignKey('templates.id'), nullable=False)
    field_id: Mapped[int] = mapped_column(ForeignKey('fields.id'), nullable=False)
    template: Mapped['TemplateModel'] = relationship(back_populates='fields')
    field: Mapped['FieldModel'] = relationship(back_populates='template_fields')

    position: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    cols: Mapped[int] = mapped_column(Integer(), nullable=True, default=None)
    is_required: Mapped[bool] = mapped_column(Boolean(), default=False)
    is_hidden: Mapped[bool] = mapped_column(Boolean(), default=False)
    label: Mapped[str] = mapped_column(String(128), nullable=True)
    placeholder: Mapped[str] = mapped_column(String(128), nullable=True)
    group: Mapped[str] = mapped_column(String(128), nullable=True)
