from fastapi import APIRouter, Depends, HTTPException
from models import Donation, Project, User
from auth import get_current_user
from database import db
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/donate", response_model=Project)
async def donate(donation: Donation, current_user: User = Depends(get_current_user)):
    project = db.projects.find_one({"_id": ObjectId(donation.project_id)})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not project["raising_funds"]:
        raise HTTPException(status_code=400, detail="This project is not currently accepting donations")
    
    new_funds_raised = project["funds_raised"] + donation.amount
    
    db.projects.update_one(
        {"_id": ObjectId(donation.project_id)},
        {
            "$set": {
                "funds_raised": new_funds_raised
            },
            "$push": {
                "donations": {
                    "user_id": str(current_user.id),
                    "amount": donation.amount,
                    "message": donation.message,
                    "date": datetime.utcnow()
                }
            }
        }
    )
    
    db.donations.insert_one({
        "user_id": str(current_user.id),
        "project_id": donation.project_id,
        "amount": donation.amount,
        "message": donation.message,
        "date": datetime.utcnow()
    })
    
    updated_project = db.projects.find_one({"_id": ObjectId(donation.project_id)})
    updated_project["id"] = str(updated_project["_id"])
    return Project(**updated_project)