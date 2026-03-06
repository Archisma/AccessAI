from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.vector_store import build_or_load_vectorstore
from backend.ai_teacher import ask_adhd_teacher



app = FastAPI(title="AccessAI ADHD Teacher API")

# Allow frontend to call backend (hackathon-friendly)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for hackathon demo; tighten later
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load vector DB once at startup
vectorstore = build_or_load_vectorstore()


class AskRequest(BaseModel):
    question: str
    mode: str  # "math" | "english" | "cognitive" | "gk"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(req: AskRequest):
    result = ask_adhd_teacher(
        question=req.question,
        mode=req.mode,
        vectorstore=vectorstore
    )
    return result
