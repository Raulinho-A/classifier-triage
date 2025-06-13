from app.classifier.validator import validate
from app.classifier.triage_input import TriageInput
from app.classifier.model_loader import pipeline_rf

def run_model(input_data: TriageInput) -> dict:
    input_dict = input_data.model_dump()
    df_validated = validate(input_dict)
    prediction = pipeline_rf.predict(df_validated)[0]
    return {
        "emergency_status": prediction,
        "message": "Emergencia" if prediction == 1 else "No emergencia"
    }