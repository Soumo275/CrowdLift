from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models import Project, ProjectCreate, User
from auth import get_current_user
from database import db
from bson import ObjectId
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/", response_model=Project)
async def create_project(project: ProjectCreate, current_user: User = Depends(get_current_user)):
    try:
        project_dict = project.dict()
        project_dict["owner_id"] = str(current_user.id)
        result = db.projects.insert_one(project_dict)
        project_dict["id"] = str(result.inserted_id)
        return Project(**project_dict)
    except Exception as e:
        logger.error(f"Error creating project: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/", response_model=List[Project])
async def get_projects():
    projects = list(db.projects.find({"raising_funds": True}))
    for project in projects:
        project["id"] = str(project["_id"])
    return projects

@router.get("/user", response_model=List[Project])
async def get_user_projects(current_user: User = Depends(get_current_user)):
    projects = list(db.projects.find({"owner_id": str(current_user.id)}))
    for project in projects:
        project["id"] = str(project["_id"])
    return projects

@router.put("/{project_id}", response_model=Project)
async def update_project(project_id: str, project: ProjectCreate, current_user: User = Depends(get_current_user)):
    existing_project = db.projects.find_one({"_id": ObjectId(project_id), "owner_id": str(current_user.id)})
    if not existing_project:
        raise HTTPException(status_code=404, detail="Project not found or you don't have permission to edit")
    
    updated_project = project.dict()
    db.projects.update_one({"_id": ObjectId(project_id)}, {"$set": updated_project})
    
    updated_project["id"] = project_id
    updated_project["owner_id"] = str(current_user.id)
    return Project(**updated_project)