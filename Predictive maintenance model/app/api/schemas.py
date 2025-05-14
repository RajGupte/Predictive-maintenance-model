from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

# Existing prediction input schema
class PredictionInput(BaseModel):
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float

# New schemas for enhanced features
class AssetBase(BaseModel):
    name: str
    type: str
    location: str
    status: str
    health_score: float
    specifications: Dict[str, Any]

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    id: int
    last_maintenance: datetime
    next_maintenance: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class MaintenanceRecordBase(BaseModel):
    maintenance_type: str
    description: str
    technician: str
    cost: float
    status: str

class MaintenanceRecordCreate(MaintenanceRecordBase):
    asset_id: int

class MaintenanceRecord(MaintenanceRecordBase):
    id: int
    asset_id: int
    created_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True

class SensorDataBase(BaseModel):
    sensor_type: str
    value: float
    unit: str

class SensorDataCreate(SensorDataBase):
    asset_id: int

class SensorData(SensorDataBase):
    id: int
    asset_id: int
    timestamp: datetime
    is_anomaly: bool

    class Config:
        from_attributes = True

class EnergyData(BaseModel):
    asset_id: int
    consumption: float
    unit: str
    cost: float
    timestamp: datetime

class AssetData(BaseModel):
    asset_id: int
    sensor_readings: List[Dict[str, float]]
    maintenance_history: List[Dict[str, Any]]
    current_status: str 