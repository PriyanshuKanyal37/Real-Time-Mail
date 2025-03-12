import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# JSearch API Key
JSEARCH_API_KEY = os.getenv("JSEARCH_API_KEY")

# Email API Key (to be used later)
EMAIL_API_KEY = os.getenv("EMAIL_API_KEY")
