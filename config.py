import os
from pathlib import Path
from dotenv import load_dotenv

# Loading env vars
load_dotenv()

# API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Models
DEFAULT_MODEL = "gemini-2.5-flash"
#IMAGE_MODEL = "veo-2"
temp = 0