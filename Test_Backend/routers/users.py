from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models import User, UserCreate, Token
from auth import authenticate_user, create_access_token, get_current_user, get_password_hash
from database import db
from config import settings
from datetime import timedelta
from bson  import ObjectId

router = APIRouter()

@router.post("/register", response_model=User)
async def register(user: UserCreate):
    if db.users.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    result = db.users.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return User(**user_dict)

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/user/investments", response_model=list[dict])
async def get_user_investments(current_user: User = Depends(get_current_user)):
    donations = list(db.donations.find({"user_id": current_user.id}))
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