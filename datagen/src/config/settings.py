import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Microservizio di Validazione"
    API_VERSION: str = "v1"
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "True") == "True"

settings = Settings()
