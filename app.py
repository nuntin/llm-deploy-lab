# app.py
from fastapi import FastAPI
from vllm import LLM

app = FastAPI()
llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1")

@app.get("/predict")
def predict(prompt: str):
    output = llm.generate(prompt)
    return {"response": output}