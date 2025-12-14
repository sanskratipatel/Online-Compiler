import os
from dotenv import load_dotenv

load_dotenv()

DB_FILE = os.getenv("DB_FILE", "app.db")
EXECUTION_TIMEOUT = int(os.getenv("EXECUTION_TIMEOUT", 5))
MAX_MEMORY = os.getenv("MAX_MEMORY", "128m")
