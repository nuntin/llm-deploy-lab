from fastapi import FastAPI, Request
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

# Load a medium-size public LLM model for text generation
pipe = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", device=-1)

# Define the input schema for POST requests
class Prompt(BaseModel):
    prompt: str

# Define the /generate endpoint
@app.post("/generate")
def generate_text(request: Prompt):
    result = pipe(request.prompt, max_length=100, do_sample=True)
    return {"result": result[0]['generated_text']}