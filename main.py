from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI(
    title="FastAPI LMS",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact = {
        "name": "SomeGuy",
        "email": "someemail@gmail.com"
    },
    license_info={
        "name": "MIT"
    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_users():
    return users



@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


# path params
# query params
@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve.,", gt=0),
    q: str = Query(None, max_length=5)
    ):
    return { "user": users[id], "query": q }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)