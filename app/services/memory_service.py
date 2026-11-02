import os

from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in .env")

DB_NAME = "persistent_chatbot_db"
COLLECTION_NAME = "chat_history"


# Load and save chat messages
def get_chat_history(session_id: str):

    return MongoDBChatMessageHistory(
        connection_string=MONGODB_URI,
        session_id=session_id,
        database_name=DB_NAME,
        collection_name=COLLECTION_NAME,
        history_size=20
    )


# Retrieve all saved conversation IDs
def list_saved_sessions():

    client = MongoClient(
        MONGODB_URI,
        serverSelectionTimeoutMS=5000
    )

    try:
        collection = client[DB_NAME][COLLECTION_NAME]

        session_ids = collection.distinct("SessionId")

        return sorted(str(session_id) for session_id in session_ids)

    finally:
        client.close()