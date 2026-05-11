from pydantic import BaseModel


class TaskFull(BaseModel):
    id: int
    name: str
    description: str | None
    checked: bool
    user_id: int


class TaskCreateReq(BaseModel):
    name: str
    description: str | None = None

    model_config = {"extra": "forbid"}


class TaskUpdReq(BaseModel):
    name: str | None = None
    description: str | None = None
    checked: bool | None = None

    model_config = {"extra": "forbid"}
