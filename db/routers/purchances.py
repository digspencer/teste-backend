# db/routers/vehicles.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import DimVehicle
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

class VehicleCreate(BaseModel):
    model: str
    prod_date: str
    year: int
    propulsion: str

class VehicleOut(BaseModel):
    vehicle_id: int
    model: str
    prod_date: str
    year: int
    propulsion: str

    class Config:
        orm_mode = True

@router.post("/", response_model=VehicleOut)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = DimVehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@router.get("/", response_model=List[VehicleOut])
def list_vehicles(db: Session = Depends(get_db)):
    return db.query(DimVehicle).all()

@router.get("/{vehicle_id}", response_model=VehicleOut)
def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    return db.query(DimVehicle).filter(DimVehicle.vehicle_id == vehicle_id).first()

@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = db.query(DimVehicle).filter(DimVehicle.vehicle_id == vehicle_id).first()
    if vehicle:
        db.delete(vehicle)
        db.commit()
        return {"msg": "Vehicle deleted successfully"}
    return {"msg": "Vehicle not found"}
