from fastapi import APIRouter, HTTPException
from app.classifier.triage_input import TriageInput
from app.classifier.classifier import run_model

router = APIRouter()

@router.post("/predict")
def classify_triage(input_data: TriageInput):
    try:
        return run_model(input_data)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")