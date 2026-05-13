from pydantic import BaseModel


class UserFull(BaseModel):
    id: int
    email: str
    role: str


class UserRegReq(BaseModel):
    email: str
    password: str
    role: str | None = None

    model_config = {"extra": "forbid"}


class UserUpdReq(BaseModel):
    password: str | None = None
    role: str | None = None

    model_config = {"extra": "forbid"}


class UserFind(BaseModel):
    id: int | None = None
    email: str | None = None