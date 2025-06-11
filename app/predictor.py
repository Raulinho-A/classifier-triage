import joblib
from pathlib import Path
from app.schemas import TriageInput

# model_path = Path(__file__).parent / "model" / "emergency_model.pkl"
# model = joblib.load(model_path)

def predict_severity(data: TriageInput) -> str:
    features = [
        data.sex,
        data.age,
        data.arrival_mode,
        data.injury,
        data.mental,
        data.pain,
        data.nrs_pain,
        data.sbp,
        data.dbp,
        data.hr,
        data.rr,
        data.bt
        # `chief_complain` no se incluye en este modelo numérico base,
        # pero podría usarse en un modelo NLP o transformarse a one-hot/tokenizado
    ]

    return features
    # pred = model.predict([features])[0]
    # return pred