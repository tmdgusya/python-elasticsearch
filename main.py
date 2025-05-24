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

@app.get("/users")
async def list_users():
    response = await client.search(index="users", query={"match_all": {}})
    user_docs = []
    for hit in response['hits']['hits']:
        id = hit['_id']
        source = hit['_source']
        user_doc = UserDocument(id=id, name=source['name'], age=source['age'], is_active=source.get('is_active', False))
        user_docs.append(user_doc)
    return {"users": user_docs}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    response = await client.get(index="users", id=user_id)
    if response['found']:
        user_doc = UserDocument(**response['_source'])
        return {"user": user_doc}
    else:
        return {"message": "User not found"}, 404
    
@app.put("/users/{user_id}")
async def update_user(user_id: str, user: UserCreateRequestDto):
    user_doc = UserDocument(
        id=user_id,
        name=user.name,
        age=user.age,
        is_active=user.is_active
    )
    response = await client.update(
        index="users",
        id=user_id,
        doc=user_doc.__dict__
    )
    if response['result'] == 'updated':
        return {"message": "User updated", "user": user_doc}
    else:
        return {"message": "User not found"}, 404
    
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    response = await client.delete(index="users", id=user_id)
    if response['result'] == 'deleted':
        return {"message": "User deleted"}
    else:
        return {"message": "User not found"}, 404