from pymongo import MongoClient
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["crowdfunding_db"]

# Test the connection
try:
    db.command('ping')
    logger.debug("MongoDB connection is active")
except Exception as e:
    logger.error(f"MongoDB connection error: {str(e)}")