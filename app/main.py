from fastapi import FastAPI
from app.schemas import TriageInput
from app.predictor import predict_severity

app = FastAPI()

#http://127.0.0.1:8000

@app.post("/predict")
def classify_triage(input_data: TriageInput):
    severity = predict_severity(input_data)
    # return {"severity": severity}
    return "triage recibido!"

