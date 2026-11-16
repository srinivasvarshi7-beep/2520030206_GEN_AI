
import os
import time
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

load_dotenv()


class UsageLogger:
    def __init__(self):
        mongodb_uri = os.getenv("MONGODB_URI")

        if not mongodb_uri:
            raise ValueError("MONGODB_URI is missing from .env")

        self.client = MongoClient(
            mongodb_uri,
            serverSelectionTimeoutMS=10000,
            connectTimeoutMS=10000,
            socketTimeoutMS=10000
        )

        self.db = self.client["llm_monitoring"]
        self.collection = self.db["api_usage"]

    def connect(self):
        self.client.admin.command("ping")
        print("MongoDB connected successfully!")

    def log_usage(self, record):
        for attempt in range(3):
            try:
                self.collection.insert_one(record)
                print("Usage record saved successfully!")
                return True

            except PyMongoError as error:
                print(f"Logging attempt {attempt + 1} failed: {error}")

                if attempt < 2:
                    time.sleep(2 ** attempt)

        return False

    def close(self):
        self.client.close()
