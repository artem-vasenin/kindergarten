from pydantic import BaseModel


class UserFull(BaseModel):
    id: int
    email: str
    password: str
    role: str


class UserRegReq(BaseModel):
    email: str
    password: str

    model_config = {"extra": "forbid"}


class UserUpdReq(BaseModel):
    email: str | None = None
    password: str | None = None

    model_config = {"extra": "forbid"}