import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = str(os.getenv("MONGO_URI"))
MONGO_DB = str(os.getenv("MONGO_DB"))

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
