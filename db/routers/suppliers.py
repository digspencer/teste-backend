from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import DimSuplier
from pydantic import BaseModel
from typing import List


router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

class SupplierCreate(BaseModel):
    suplier_name: str
    location_id: int

class SupplierOut(BaseModel):
    suplier_id: int
    suplier_name: str
    location_id: int

    class Config:
        orm_mode = True

# 🔹 Bulk insert
@router.post("/bulk")
def create_suppliers_bulk(suppliers: List[SupplierCreate], db: Session = Depends(get_db)):
    objs = [DimSuplier(**supplier.dict()) for supplier in suppliers]
    db.bulk_save_objects(objs)
    db.commit()
    return {"msg": f"{len(objs)} suppliers created"}

# 🔹 List with optional filter
@router.get("/", response_model=List[SupplierOut])
def list_suppliers(name: str = "", db: Session = Depends(get_db)):
    query = db.query(DimSuplier)
    if name:
        query = query.filter(DimSuplier.suplier_name.ilike(f"%{name}%"))
    return query.all()
