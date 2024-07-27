from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models import Donation, User
from auth import get_current_user
from database import db
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/")
async def donate(donation: Donation, current_user: User = Depends(get_current_user)):
    project = db.projects.find_one({"_id": ObjectId(donation.project_id), "raising_funds": True})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found or not raising funds")
    
    new_funds_raised = project["funds_raised"] + donation.amount
    new_progress = (new_funds_raised / project["fundraising_goal"]) * 100
    
    db.projects.update_one(
        {"_id": ObjectId(donation.project_id)},
        {"$set": {"funds_raised": new_funds_raised, "progress": new_progress}}
    )
    
    db.donations.insert_one({
        "user_id": str(current_user.id),
        "project_id": donation.project_id,
        "amount": donation.amount,
        "date": datetime.utcnow()
    })
    
    return {"message": "Donation successful"}

@router.get("/user/investments", response_model=List[dict])
async def get_user_investments(current_user: User = Depends(get_current_user)):
    donations = list(db.donations.find({"user_id": str(current_user.id)}))
    investments = []
    for donation in donations:
        project = db.projects.find_one({"_id": ObjectId(donation["project_id"])})
        if project:
            investments.append({
                "project_id": str(project["_id"]),
                "title": project["title"],
                "amount_invested": donation["amount"],
                "date": donation["date"]
            })
    return investments