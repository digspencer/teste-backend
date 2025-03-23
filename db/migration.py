from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os
from dotenv import load_dotenv


load_dotenv()

def run_migration():
    engine = create_engine(os.getenv('CONN_STRING'))
    Base.metadata.create_all(engine)
    print("Done!")

run_migration()