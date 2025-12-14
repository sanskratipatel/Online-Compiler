from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal
from backend.app.models import CodeSnippet

router = APIRouter(prefix="/api/snippets")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def save_snippet(language: str, code: str, db: Session = Depends(get_db)):
    snippet = CodeSnippet(language=language, code=code)
    db.add(snippet)
    db.commit()
    db.refresh(snippet)
    return snippet

@router.get("/")
def list_snippets(db: Session = Depends(get_db)):
    return db.query(CodeSnippet).all()
