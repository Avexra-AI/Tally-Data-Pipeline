import os
from dotenv import load_dotenv

load_dotenv()

import os

SUPABASE_DATABASE_URL = os.getenv("SUPABASE_DATABASE_URL")
CONNECTOR_TOKEN = os.getenv("CONNECTOR_TOKEN")
RAW_STORAGE_PATH = os.getenv("RAW_STORAGE_PATH", "storage/raw")

