from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str


class UserResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id: int


class LoginSchema(BaseModel):
    username: str
    password: str
