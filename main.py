from uuid import uuid4
from dataclasses import dataclass
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from user_dto import UserCreateRequestDto

client = AsyncElasticsearch(
    "http://localhost:9200",
    api_key="api_key",
)

@dataclass
class UserDocument:
    id: str # id
    name: str # fieldType.keyword
    age: int # fieldType.long
    is_active: bool # fieldType.boolean
    
app = FastAPI()

@app.post("/users/")
async def create_user(user: UserCreateRequestDto):
    user_doc = UserDocument(
        id=str(uuid4()),
        name=user.name,
        age=user.age,
        is_active=user.is_active
    )
    response = await client.index(
        index="users",
        id=user_doc.id,
        document=user_doc.__dict__
    )
    print(response)
    await client.indices.refresh(index="users")
    return {"message": "User created", "user": user_doc}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    response = await client.get(index="users", id=user_id)
    if response['found']:
        user_doc = UserDocument(**response['_source'])
        return {"user": user_doc}
    else:
        return {"message": "User not found"}, 404