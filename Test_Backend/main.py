from fastapi import FastAPI
from routers import users, projects, donations
app = FastAPI()

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(donations.router)