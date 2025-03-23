from sqlalchemy import create_engine, text

from .db.models import Base, FactWarranties

engine = create_engine("postgresql+psycopg2://postgres:testeford@localhost:5432/postgres")




