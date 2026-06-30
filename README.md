# Attack Detection API

A FastAPI-based REST API that serves a trained Random Forest machine learning model for Wi-Fi attack detection.

## Overview

This API receives Wi-Fi network features, preprocesses the input, and predicts whether the traffic is **Normal** or an **Attack**.

## Features

- FastAPI REST API
- Random Forest prediction model
- Probability scores for predictions
- Interactive Swagger documentation
- Ready for deployment on Render

## Project Structure

```
AI_Model_API/
│── app.py
│── attack_detection_model.pkl
│── requirements.txt
│── runtime.txt
│── README.md
└── .gitignore
```

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd AI_Model_API
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check if the API is running |
| POST | `/predict` | Predict whether traffic is normal or an attack |

## Example Request

```json
{
  "wlan_bssid": 652,
  "wlan_sa": 758,
  "wlan_radio_channel": 0.461729,
  "radiotap_dbm_antsignal": -0.592966,
  "wlan_fc_protected": 0.240472,
  "frame_len": -0.901852,
  "wlan_fc_retry": -0.462,
  "wlan_duration": 0.35,
  "wlan_seq": 0.12,
  "connected_clients": 3
}
```

## Example Response

```json
{
  "prediction": 1,
  "prediction_name": "attack",
  "attack_probability": 0.84
}
```

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Uvicorn

## Deployment

This API can be deployed locally, exposed using ngrok for testing, or hosted permanently using Render.

## Authors

- Shahd Mostafa