from fastapi import FastAPI
from routers import users, projects, donations
from database import db

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(donations.router, prefix="/donations", tags=["donations"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)