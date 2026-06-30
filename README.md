# Attack Detection API

A FastAPI-based REST API that serves a trained Random Forest machine learning model for Wi-Fi attack detection. The API receives network traffic features and predicts whether the traffic is **Normal** or an **Attack**.

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
│── app.py
│── attack_detection_model.pkl
│── requirements.txt
│── runtime.txt
│── README.md
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

---

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

---

## Example Response

```json
{
  "prediction": 1
}
```

Where:

- `0` = Normal Traffic
- `1` = Attack Detected

---

## Deployment

The API is deployed on **Render** and can be accessed through the generated Render URL.

---

## Raspberry Pi Integration

The Raspberry Pi sends network traffic features to the API using an HTTP POST request.

Example:

```python
import requests

url = "https://your-render-url.onrender.com/predict"

response = requests.post(url, json=payload)

print(response.json())
```

---

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
