from pydantic import BaseModel

class UserCreateRequestDto(BaseModel):
    name: str
    age: int
    is_active: bool