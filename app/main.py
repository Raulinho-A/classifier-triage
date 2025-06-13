from fastapi import FastAPI
from app.api.controller import router as triage_router

app = FastAPI()

#http://127.0.0.1:8000

app.include_router(triage_router, prefix="/api")
