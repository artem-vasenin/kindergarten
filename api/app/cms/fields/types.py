from typing import Any

from pydantic import BaseModel, Field
from enum import Enum


class FieldEnum(str, Enum):
    STR = 'str'
    INT = 'int'
    FLOAT = 'float'
    DATETIME = 'datetime'
    BOOL = 'bool'
    FILES = 'files'
    REPEATER = 'repeater'
    BLOCKS = 'blocks'
    JSON = 'json'


class FieldType(BaseModel):
    id: int
    name: str
    description: str
    field_type: FieldEnum
    default_value: dict | None
    settings: dict[str, Any] = Field(default_factory=dict)

    model_config = {
        'from_attributes': True,
    }


class FieldCreateType(BaseModel):
    name: str
    description: str | None = None
    field_type: FieldEnum
    default_value: Any | None = None
    settings: dict[str, Any] = Field(default_factory=dict)


class FieldUpdateType(BaseModel):
    name: str | None = None
    description: str | None = None
    default_value: Any | None = None
