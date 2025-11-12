from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv
load_dotenv()
from networksecurity.logging.logger import logging

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

uri = MONGO_DB_URL
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    logging.info("Connected to Mongodb database successfully")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)