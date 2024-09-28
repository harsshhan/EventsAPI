from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

uri = os.getenv("DB_URL")

client = MongoClient(uri)

db=None

try:
    db=client[os.getenv("DB_NAME")]
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

if db is None:
    raise ValueError("Database connection was not established.")