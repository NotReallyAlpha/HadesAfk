from config import DB
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo = MongoClient(DB.MONGO_DB_URL)
db = mongo.AFK
