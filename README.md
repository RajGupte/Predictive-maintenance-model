
# 🛠️ Enhanced Predictive Maintenance API

A production-grade **FastAPI** project that powers an AI-driven facility and asset management platform. This system integrates multiple machine learning models—including predictive maintenance, anomaly detection, and energy optimization—while supporting full CRUD functionality for assets and sensor data.

![System Overview](Figure_1.png)

---

## 🔧 Features

- 🔮 Predictive Maintenance (LSTM or similar logic)
- ⚠️ Anomaly Detection in sensor readings
- ⚡ Energy Consumption Optimization
- 📦 CRUD operations for Assets, Sensor Data & Maintenance Records
- 📊 Integrated with LightGBM for failure prediction
- 🌐 REST API built using FastAPI and SQLAlchemy
- 🎛️ Modular ML integration with Streamlit visualization support (optional)

---

## 🧠 Tech Stack

| Component       | Technology                   |
|----------------|------------------------------|
| Backend API     | FastAPI                      |
| Database        | SQLAlchemy + SQLite / Postgres |
| ML Models       | LightGBM, TensorFlow, scikit-learn |
| Validation      | Pydantic                     |
| Deployment      | Uvicorn                      |
| Optional Tools  | Streamlit, Docker            |

---

## 📂 Project Structure

```
project-root/
│
├── main.py                    # FastAPI app with all routes
├── database.py                # DB setup using SQLAlchemy
├── models.py                  # SQLAlchemy ORM models
├── schemas.py                 # Pydantic schemas
├── requirements.txt           # All dependencies
│
├── ml_models/
│   ├── predictive_maintenance.py
│   ├── anomaly_detection.py
│   └── energy_optimization.py
│
├── utils/
│   └── predict.py             # LightGBM prediction function
│
└── Figure_1.png               # System architecture diagram
```

---

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/predictive-maintenance-api.git
cd predictive-maintenance-api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables
Create a `.env` file in the root folder:
```
DATABASE_URL=sqlite:///./facility_management.db
```

### 4. Start the API
```bash
uvicorn main:app --reload
```

### 5. Test it in your browser
Visit: `http://127.0.0.1:8000/docs`

---

## 📬 API Endpoints

| Method | Endpoint                    | Description                            |
|--------|-----------------------------|----------------------------------------|
| POST   | `/predict/`                 | Predict failure using LightGBM         |
| POST   | `/maintenance/predict`      | Predict time-to-failure (LSTM)         |
| POST   | `/anomaly/detect`           | Detect sensor anomalies                |
| POST   | `/energy/optimize`          | Recommend energy optimization actions  |
| CRUD   | `/assets/`, `/sensor_data/` | Manage asset and sensor records        |

---

## 📊 Example Input (LightGBM Prediction)

```json
{
  "air_temperature": 300.5,
  "process_temperature": 310.2,
  "rotational_speed": 1500,
  "torque": 45.0,
  "tool_wear": 10.5
}
```

---

## 🎯 Future Enhancements

- Streamlit Dashboard Integration
- JWT-based Auth System
- Historical analytics & reporting
- Model versioning with MLflow

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Raj Gupte**  
📧 mrrajgupte5@gmail.com  

