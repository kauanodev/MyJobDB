from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

load_dotenv()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = "MyJobDB"

TEMPLATES = Jinja2Templates(directory=APP_ROOT + "/templates")

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

BACKEND_CORS_ORIGINS = ["localhost:3000"]
