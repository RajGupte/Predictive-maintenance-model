from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine
from ml_models.predictive_maintenance import PredictiveMaintenanceModel
from ml_models.anomaly_detection import AnomalyDetectionModel
from ml_models.energy_optimization import EnergyOptimizationModel
from utils.predict import load_model, predict_failure

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enhanced Predictive Maintenance API",
    description="API for AI-powered facility and asset management system",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize ML models
predictive_model = PredictiveMaintenanceModel()
anomaly_model = AnomalyDetectionModel()
energy_model = EnergyOptimizationModel()
lightgbm_model = load_model()  # Your existing LightGBM model

@app.get("/")
async def root():
    return {"message": "Welcome to Enhanced Predictive Maintenance API"}

# Existing LightGBM prediction endpoint
@app.post("/predict/")
async def predict(data: schemas.PredictionInput):
    try:
        prediction = predict_failure(lightgbm_model, data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# New endpoints for enhanced features
@app.post("/maintenance/predict")
async def predict_maintenance(asset_data: schemas.AssetData):
    prediction = predictive_model.predict(asset_data)
    return {"prediction": prediction}

@app.post("/anomaly/detect")
async def detect_anomaly(sensor_data: schemas.SensorData):
    anomaly = anomaly_model.detect(sensor_data)
    return {"anomaly_detected": anomaly}

@app.post("/energy/optimize")
async def optimize_energy(energy_data: schemas.EnergyData):
    optimization = energy_model.optimize(energy_data)
    return {"optimization": optimization}

@app.post("/assets/", response_model=schemas.Asset)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = models.Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.get("/assets/", response_model=List[schemas.Asset])
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    assets = db.query(models.Asset).offset(skip).limit(limit).all()
    return assets

@app.get("/assets/{asset_id}", response_model=schemas.Asset)
def read_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 