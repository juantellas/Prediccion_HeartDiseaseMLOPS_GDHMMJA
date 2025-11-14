from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import json
import os

app = FastAPI(title="Heart Disease Prediction API", version="1.0")

MODEL_PATH = "app/model.joblib"
FEATURES_PATH = "app/feature_names.json"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("❌ No se encontró el modelo entrenado en app/model.joblib")

model = joblib.load(MODEL_PATH)

with open(FEATURES_PATH, "r") as f:
    feature_names = json.load(f)

class HeartData(BaseModel):
    Age: float
    RestingBP: float
    Cholesterol: float
    MaxHR: float
    Oldpeak: float
    Sex_M: int
    ChestPainType_ATA: int
    ChestPainType_NAP: int
    ChestPainType_TA: int
    FastingBS_1: int
    RestingECG_Normal: int
    RestingECG_ST: int
    ExerciseAngina_Y: int
    ST_Slope_Flat: int
    ST_Slope_Up: int

@app.get("/")
def root():
    return {"message": "💓 Heart Disease Prediction API is running"}

@app.post("/predict")
def predict(data: HeartData):
    df = pd.DataFrame([data.model_dump()], columns=feature_names)

    pred_prob = model.predict_proba(df)[0, 1]
    pred_label = "Heart Disease" if pred_prob > 0.5 else "No Heart Disease"

    return {
        "heart_disease_probability": round(float(pred_prob), 3),
        "heart_disease_prediction": pred_label
    }
