from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Vigilant AI ML Service")

class TextData(BaseModel):
    text: str

def get_scam_score(text: str):
    """Placeholder for Logistic Regression Model"""
    text_lower = text.lower()
    # Logic mimicking Phase 1 weights
    if "ksh" in text_lower and "received" in text_lower:
        return 0.95 
    if "pin" in text_lower or "reversal" in text_lower:
        return 0.85
    return 0.10

@app.get("/")
def health():
    return {"status": "ML Service Online", "model": "Vigilant-AI-Africa-v1"}

@app.post("/predict")
def predict(data: TextData):
    score = get_scam_score(data.text)
    return {
        "confidence_score": score,
        "is_scam_likely": score > 0.5
    }
