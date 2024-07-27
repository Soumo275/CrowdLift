from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models import Project, ProjectCreate, User
from auth import get_current_user
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/projects", response_model=Project)
async def create_project(project: ProjectCreate, current_user: User = Depends(get_current_user)):
    project_dict = project.dict()
    project_dict["owner_id"] = str(current_user.id)
    result = db.projects.insert_one(project_dict)
    project_dict["id"] = str(result.inserted_id)
    return Project(**project_dict)

@router.get("/projects", response_model=List[Project])
async def get_projects():
    projects = list(db.projects.find({"raising_funds": True}))
    for project in projects:
        project["id"] = str(project["_id"])
    return projects

@router.put("/projects/{project_id}", response_model=Project)
async def update_project(project_id: str, project_update: ProjectCreate, current_user: User = Depends(get_current_user)):
    existing_project = db.projects.find_one({"_id": ObjectId(project_id), "owner_id": str(current_user.id)})
    if not existing_project:
        raise HTTPException(status_code=404, detail="Project not found or you don't have permission to update it")
    
    update_data = project_update.dict(exclude_unset=True)
    db.projects.update_one({"_id": ObjectId(project_id)}, {"$set": update_data})
    
    updated_project = db.projects.find_one({"_id": ObjectId(project_id)})
    updated_project["id"] = str(updated_project["_id"])
    return Project(**updated_project)

@router.get("/user/projects", response_model=List[Project])
async def get_user_projects(current_user: User = Depends(get_current_user)):
    user_projects = list(db.projects.find({"owner_id": str(current_user.id)}))
    for project in user_projects:
        project["id"] = str(project["_id"])
    return [Project(**project) for project in user_projects]