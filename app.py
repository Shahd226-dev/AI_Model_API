from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

# ==========================================================
# Create FastAPI Application
# ==========================================================

app = FastAPI(
    title="Wi-Fi Attack Detection API",
    description="Random Forest API for Wi-Fi Attack Detection",
    version="2.0.0"
)

# ==========================================================
# Load Trained Model
# ==========================================================

MODEL_PATH = "Models/random_forest_optimized.pkl"

try:
    model = joblib.load(MODEL_PATH)
    print("===================================")
    print("Random Forest model loaded.")
    print("API Ready.")
    print("===================================")
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# ==========================================================
# Request Model
# ==========================================================

class PredictionRequest(BaseModel):
    wlan_radio_channel: float
    radiotap_dbm_antsignal: float
    wlan_fc_protected: float
    connected_clients: float

# ==========================================================
# Home Endpoint
# ==========================================================

@app.get("/")
def home():
    return {
        "message": "Wi-Fi Attack Detection API is Running",
        "model": "Random Forest",
        "version": "2.0.0"
    }

# ==========================================================
# Health Endpoint
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }

# ==========================================================
# Prediction Endpoint
# ==========================================================

@app.post("/predict")
def predict(request: PredictionRequest):

    try:

        # Create DataFrame with EXACT feature names used during training
        data = pd.DataFrame([{
            "wlan_radio.channel": request.wlan_radio_channel,
            "radiotap.dbm_antsignal": request.radiotap_dbm_antsignal,
            "wlan.fc.protected": request.wlan_fc_protected,
            "Connected_Clients": request.connected_clients
        }])

        # Prediction
        prediction = model.predict(data)[0]

        # Prediction Probabilities
        probabilities = model.predict_proba(data)[0]

        response = {
            "prediction": int(prediction),
            "prediction_name": "Attack" if prediction == 0 else "Normal",
            "attack_probability": round(float(probabilities[0]), 4),
            "normal_probability": round(float(probabilities[1]), 4)
        }

        return response

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )