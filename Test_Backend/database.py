from pymongo import MongoClient
from config import settings

client = MongoClient("mongodb://localhost:27017")
db = client["crowdfunding_db"]