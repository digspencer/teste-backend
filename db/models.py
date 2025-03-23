from sqlalchemy import (
    Column, Integer, String, Date, Text, Enum, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import declarative_base


import enum

Base = declarative_base()

class PropulsionType(enum.Enum):
    eletric = 'eletric'
    hybrid = 'hybrid'
    gas = 'gas'

class PurchanceType(enum.Enum):
    bulk = 'bulk'
    warranty = 'warranty'

class DimLocations(Base):
    __tablename__ = 'Dim_locations'

    location_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    market = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

class DimSuplier(Base):
    __tablename__ = 'Dim_Suplier'

    suplier_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    suplier_name = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey('Dim_locations.location_id'), nullable=False)

class DimVehicle(Base):
    __tablename__ = 'Dim_Vehicle'

    vehicle_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    model = Column(String(255), nullable=False)
    prod_date = Column(Date, nullable=False)
    year = Column(Integer, nullable=False)
    propulsion = Column(Enum(PropulsionType), nullable=False)

class DimPurchances(Base):
    __tablename__ = 'Dim_purchances'

    purchance_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    purchance_type = Column(Enum(PurchanceType), nullable=False)
    purchance_date = Column(Date, nullable=False)
    part_id = Column(Integer, ForeignKey('Dim_Parts.part_id'), nullable=False)

class DimParts(Base):
    __tablename__ = 'Dim_Parts'

    part_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    part_name = Column(String(255), nullable=False)
    last_id_purchase = Column(Integer, ForeignKey('Dim_purchances.purchance_id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('Dim_Suplier.suplier_id'), nullable=False)

class FactWarranties(Base):
    __tablename__ = 'Fact_Warranties'

    vehicle_id = Column(Integer, ForeignKey('Dim_Vehicle.vehicle_id'), nullable=False, unique=True)
    claim_key = Column(Integer, primary_key=True, autoincrement=True)
    repair_date = Column(Date, nullable=False)
    client_comment = Column(Text)
    tech_comment = Column(Text, nullable=False)
    part_id = Column(Integer, ForeignKey('Dim_Parts.part_id'), nullable=False)
    classifed_failured = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey('Dim_locations.location_id'), nullable=False)
    purchance_id = Column(Integer, ForeignKey('Dim_purchances.purchance_id'), nullable=False)
