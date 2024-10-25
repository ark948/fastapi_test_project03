from fastapi import FastAPI
from api import users, sections, courses
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.creae_all(bind=engine)

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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)