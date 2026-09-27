from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URL"))

db = client["signupDB"]
collection = db["users"]

try:
    client.admin.command('ping')
    print("Connected to MongoDB Atlas successfully!")
except Exception as e:
    print("Connection failed:", e)