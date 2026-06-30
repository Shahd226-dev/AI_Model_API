from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

# ==========================
# Create FastAPI application
# ==========================

app = FastAPI(
    title="Attack Detection API",
    description="API for detecting normal vs attack Wi-Fi traffic",
    version="1.0.0"
)

# ==========================
# Load trained model
# ==========================

artifact = joblib.load("attack_detection_model.pkl")

model = artifact["model"]
scaler = artifact["scaler"]
feature_columns = artifact["feature_columns"]
numeric_columns = artifact["numeric_columns"]

# ==========================
# Request Model
# ==========================

class PredictionRequest(BaseModel):
    wlan_bssid: int
    wlan_sa: int
    wlan_radio_channel: float
    radiotap_dbm_antsignal: float
    wlan_fc_protected: float
    frame_len: float
    wlan_fc_retry: float
    wlan_duration: float
    wlan_seq: float
    connected_clients: float

# ==========================
# Home Endpoint
# ==========================

@app.get("/")
def home():
    return {
        "message": "Attack Detection API Running!"
    }

# ==========================
# Health Check
# ==========================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# ==========================
# Prediction Endpoint
# ==========================

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # Convert request to DataFrame
        data = pd.DataFrame([request.model_dump()])

        # Ensure feature order matches training
        data = data[feature_columns]

        # Scale only numeric columns
        data_scaled = data.copy()
        data_scaled[numeric_columns] = scaler.transform(
            data_scaled[numeric_columns]
        )

        # Predict
        prediction = model.predict(data_scaled)
        probability = model.predict_proba(data_scaled)

        return {
            "prediction": int(prediction[0]),
            "prediction_name": "attack" if prediction[0] == 1 else "normal",
            "attack_probability": round(float(probability[0][1]), 4),
            "normal_probability": round(float(probability[0][0]), 4)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )