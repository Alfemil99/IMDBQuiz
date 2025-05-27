import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

# Example: postgresql://user:password@localhost:5432/myappdb
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@localhost:5432/myappdb")
