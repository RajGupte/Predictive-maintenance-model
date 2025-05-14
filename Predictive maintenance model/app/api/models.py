from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, JSON
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    location = Column(String)
    status = Column(String)
    health_score = Column(Float)
    last_maintenance = Column(DateTime, default=datetime.datetime.utcnow)
    next_maintenance = Column(DateTime)
    specifications = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    maintenance_records = relationship("MaintenanceRecord", back_populates="asset")
    sensor_data = relationship("SensorData", back_populates="asset")

class MaintenanceRecord(Base):
    __tablename__ = "maintenance_records"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    maintenance_type = Column(String)
    description = Column(String)
    technician = Column(String)
    cost = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    completed_at = Column(DateTime)

    asset = relationship("Asset", back_populates="maintenance_records")

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    sensor_type = Column(String)
    value = Column(Float)
    unit = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    is_anomaly = Column(Boolean, default=False)

    asset = relationship("Asset", back_populates="sensor_data")

class EnergyConsumption(Base):
    __tablename__ = "energy_consumption"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    consumption = Column(Float)
    unit = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    cost = Column(Float)
    is_optimized = Column(Boolean, default=False) 