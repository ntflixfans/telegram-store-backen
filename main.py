from fastapi import FastAPI
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

client = MongoClient(MONGO_URI)
db = client.telegram_store

@app.get("/")
def read_root():
    return {"status": "Backend is running"}