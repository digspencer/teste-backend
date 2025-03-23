from fastapi import FastAPI
from db.routers import suppliers, vehicles, purchances  
from db.database import engine  
from db.models import Base  

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(suppliers.router)   
app.include_router(vehicles.router)    
app.include_router(purchances.router)  

@app.get("/")
def root():
    return {"msg": "API CRM ready"}
