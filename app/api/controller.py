from fastapi import APIRouter, HTTPException
from app.classifier.triage_input import TriageInput, BatchTriageInput
from app.classifier.classifier import run_model, run_model_batch
from app.classifier.model_loader import expected_columns, expected_types

router = APIRouter()

@router.post("/predict")
def classify_triage(input_data: TriageInput):
    try:
        return run_model(input_data)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
    
@router.post("/predict/batch")
def classify_batch(input_data: BatchTriageInput):
    try:
        input_list = [record.model_dump(by_alias=True) for record in input_data.data]
        return run_model_batch(input_list)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/schema")
def get_model_schema():
    return {
        "columns": expected_columns,
        "types": expected_types
    }