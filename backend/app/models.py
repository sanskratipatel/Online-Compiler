from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from backend.app.database import Base

class CodeSnippet(Base):
    __tablename__ = "snippets"

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String(20))
    code = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
