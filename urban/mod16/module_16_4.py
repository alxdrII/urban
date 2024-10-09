from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
users = []

ant_id = Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]
ant_name = Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
ant_age = Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: ant_name, age: ant_age):
    user_id = str(int(max(users, key=int)) + 1)
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: ant_id, username: ant_name, age: ant_age):
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@app.delete('/user/{user_id}')
async def del_user(user_id: ant_id):
    users.pop(str(user_id))
    return f"The user {user_id} has been deleted"
