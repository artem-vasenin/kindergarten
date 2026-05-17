from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any
from sqlalchemy import ForeignKey, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base import Base


if TYPE_CHECKING:
    from app.cms.templates.models import TemplateModel

class PageModel(Base):
    __tablename__ = 'pages'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    template_id: Mapped[int] = mapped_column(ForeignKey('templates.id'), nullable=False)
    template: Mapped['TemplateModel'] = relationship('TemplateModel', back_populates='pages')
    parent_id: Mapped[int | None] = mapped_column(ForeignKey('pages.id'), nullable=True)
    parent: Mapped['PageModel'] = relationship('PageModel', remote_side='PageModel.id', back_populates='children')
    children: Mapped[list['PageModel']] = relationship('PageModel', back_populates='parent')

    title: Mapped[str] = mapped_column(String(256), nullable=False)
    slug: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    path: Mapped[str] = mapped_column(String(1024), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default='draft')
    sort: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    data: Mapped[dict] = mapped_column(JSONB, nullable=False, default=lambda: {})
    published_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(), default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    def get_value(self, template_field_id: int, default=None):
        return self.data.get(str(template_field_id), default)

    def set_value(self, template_field_id: int, value):
        self.data[str(template_field_id)] = value

    def set_values(self, values: dict[int, Any]):
        for k, v in values.items():
            self.data[str(k)] = v
