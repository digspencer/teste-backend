# db/routers/purchances.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import DimPurchances
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/purchances", tags=["Purchances"])

class PurchanceCreate(BaseModel):
    purchance_type: str
    purchance_date: str
    part_id: int

class PurchanceOut(BaseModel):
    purchance_id: int
    purchance_type: str
    purchance_date: str
    part_id: int

    class Config:
        orm_mode = True

@router.post("/", response_model=PurchanceOut)
def create_purchance(purchance: PurchanceCreate, db: Session = Depends(get_db)):
    db_purchance = DimPurchances(**purchance.dict())
    db.add(db_purchance)
    db.commit()
    db.refresh(db_purchance)
    return db_purchance

@router.get("/", response_model=List[PurchanceOut])
def list_purchances(db: Session = Depends(get_db)):
    return db.query(DimPurchances).all()

@router.get("/{purchance_id}", response_model=PurchanceOut)
def get_purchance(purchance_id: int, db: Session = Depends(get_db)):
    return db.query(DimPurchances).filter(DimPurchances.purchance_id == purchance_id).first()

@router.delete("/{purchance_id}")
def delete_purchance(purchance_id: int, db: Session = Depends(get_db)):
    purchance = db.query(DimPurchances).filter(DimPurchances.purchance_id == purchance_id).first()
    if purchance:
        db.delete(purchance)
        db.commit()
        return {"msg": "Purchance deleted successfully"}
    return {"msg": "Purchance not found"}
