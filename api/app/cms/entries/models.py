from typing import TYPE_CHECKING, Any

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from app.cms.templates.models import TemplateModel

class EntryModel(Base):
    __tablename__ = 'entries'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    template_id: Mapped[int] = mapped_column(ForeignKey('templates.id'), nullable=False)
    data: Mapped[dict] = mapped_column(JSONB, nullable=False, default=dict)

    template: Mapped['TemplateModel'] = relationship(back_populates='entries')

    def get_value(self, template_field_id: int, default=None):
        return self.data.get(str(template_field_id), default)

    def set_value(self, template_field_id: int, value):
        self.data[str(template_field_id)] = value

    def set_values(self, values: dict[int, Any]):
        for k, v in values.items():
            self.data[str(k)] = v
