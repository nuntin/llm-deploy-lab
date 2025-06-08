# app.py (FastAPI)
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import logging

app = FastAPI()

# Optional: logging
logging.basicConfig(level=logging.INFO)

# Load model
pipe = pipeline("text-generation", model="sshleifer/tiny-gpt2", device=-1)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(req: PromptRequest):
    logging.info(f"📥 Prompt received: {req.prompt}")
    result = pipe(req.prompt, max_new_tokens=100)
    return {"result": result[0]["generated_text"]}