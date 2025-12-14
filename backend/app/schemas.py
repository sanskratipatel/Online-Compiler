from pydantic import BaseModel
from datetime import datetime

class CodeRunRequest(BaseModel):
    language: str
    code: str

class SnippetResponse(BaseModel):
    id: int
    language: str
    code: str
    created_at: datetime

    class Config:
        from_attributes = True
