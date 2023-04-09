import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = Path(__file__).parent
STATIC_FOLDER = BASE_PATH.joinpath("static")
TEMPLATES_FOLDER = BASE_PATH.joinpath("templates")
APP_SESSION_KEY = os.getenv("APP_SESSION_KEY") or ""

if not APP_SESSION_KEY:
    raise Exception("Missing APP_SESSION_KEY from the environment")
