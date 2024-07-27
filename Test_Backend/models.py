from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type, _handler):
        from pydantic_core import core_schema
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.is_instance_schema(ObjectId),
            serialization=core_schema.plain_serializer_function_ser_schema(str),
        )

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: str

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str}
    }

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ProjectCreate(BaseModel):
    title: str
    description: str
    fundraising_goal: float
    start_date: str
    raising_funds: bool = True
    funds_raised: float = 0
    progress: float = 0
    youtube_url: Optional[str] = None

class Project(ProjectCreate):
    id: str
    owner_id: str

class Donation(BaseModel):
    project_id: str
    amount: float
    message: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str