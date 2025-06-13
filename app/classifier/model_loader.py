import joblib
import json
from pathlib import Path
from catboost import CatBoostClassifier

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"

# RandomForest pipeline
pipeline_rf = joblib.load(MODEL_DIR / "randomforest_pipeline.pkl")

# CatBoost
model_cb = CatBoostClassifier()
model_cb.load_model(str(MODEL_DIR / "catboost_model.cbm"))

# Columnas esperadas (para validación)
with open(MODEL_DIR / "columns.json") as f:
    expected_columns = json.load(f)

# Tipos esperados por columna
with open(MODEL_DIR / "types.json") as f:
    expected_types = json.load(f)
