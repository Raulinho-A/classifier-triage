from fastapi import FastAPI
from app.api.controller import router as triage_router

app = FastAPI()

app.include_router(triage_router, prefix="/api")
