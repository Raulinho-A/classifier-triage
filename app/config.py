from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

PROJ_ROOT = Path(__file__).resolve().parents[1]

APP_DIR = PROJ_ROOT / "app"

MODEL_DIR = Path(os.getenv("MODEL_DIR", APP_DIR / "model"))

PORT = int(os.getenv("PORT", 8000))