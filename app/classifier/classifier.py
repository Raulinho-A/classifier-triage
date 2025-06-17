from app.classifier.validator import validate
from app.classifier.triage_input import TriageInput
from app.classifier.model_loader import pipeline_rf
from typing import List

def run_model(input_data: TriageInput) -> dict:
    print("Input recibido:", input_data)
    input_dict = input_data.model_dump(by_alias=True)
    df_validated = validate(input_dict)
    prediction = pipeline_rf.predict(df_validated)[0]

    result = {
        "emergency_status": int(prediction),
        "message": "Emergencia" if prediction == 1 else "No emergencia"
    }

    print("Predicción generada:", result)
    return result

def run_model_batch(input_list: List[dict]) -> List[dict]:
    results = []

    for i, item in enumerate(input_list):
        try:
            df = validate(item)
            prediction = pipeline_rf.predict(df)[0]
            results.append({
                "index": i,
                "status": "ok",
                "emergency_status": int(prediction),
                "message": "Emergencia" if prediction == 1 else "No emergencia"
            })
        except Exception as e:
            results.append({
                "index": i,
                "status": "error",
                "message": str(e)
            })

    return results