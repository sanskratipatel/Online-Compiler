from fastapi import APIRouter

# run_code.py
from backend.app.schemas import CodeRunRequest
from backend.app.services.executor import execute_code


router = APIRouter(prefix="/api")

@router.post("/run")
def run_code(payload: CodeRunRequest):
    return execute_code(payload.language, payload.code)
