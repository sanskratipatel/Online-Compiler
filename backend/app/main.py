from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.app.database import engine, Base
from backend.app.routers import run_code, snippets


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online Compiler")

app.include_router(run_code.router)
app.include_router(snippets.router)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
