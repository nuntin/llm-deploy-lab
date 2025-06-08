from transformers import pipeline

# public model no login
pipe = pipeline("text-generation", model="sshleifer/tiny-gpt2", device=-1)  # CPU-safe, no token needed

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate(prompt: Prompt):
    result = pipe(prompt.prompt, max_new_tokens=50, do_sample=True)[0]['generated_text']
    return {"result": result}
