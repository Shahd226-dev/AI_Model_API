# Attack Detection API

A FastAPI-based REST API that serves a trained Random Forest machine learning model for Wi-Fi attack detection.

## Overview

This API receives Wi-Fi network features, receives four Wi-Fi features and predicts whether the traffic is Normal or Attack using a trained Random Forest model, and predicts whether the traffic is **Normal** or an **Attack**.

## Features

- FastAPI backend
- Random Forest model (`attack_detection_model.pkl`)
- REST API for predictions
- Interactive Swagger documentation
- Ready for Raspberry Pi integration
- Deployed on Render

---

## Project Structure

```
AI_Model_API/
│
├── Models/
│      random_forest_optimized.pkl
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Shahd226-dev/AI_Model_API.git
cd AI_Model_API
```

Create and activate a virtual environment (recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Run the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint   | Description           |
| ------ | ---------- | --------------------- |
| GET    | `/`        | API information       |
| GET    | `/health`  | Health check          |
| POST   | `/predict` | Predict Attack/Normal |


## Example Request

```json
{
  "wlan_radio_channel": 36,
  "radiotap_dbm_antsignal": -45,
  "wlan_fc_protected": 1,
  "connected_clients": 12
}
```

---

## Example Response

```json
{
  "prediction": 1,
  "prediction_name": "Normal",
  "attack_probability": 0.0000,
  "normal_probability": 1.0000
}
```

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Uvicorn
- Joblib
- Render
- Git & GitHub

---

## Author

**Shahd Mostafa**
