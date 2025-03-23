from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_supplier():
    response = client.post(
        "/suppliers/bulk", 
        json=[
            {"suplier_name": "Supplier A", "location_id": 1},
            {"suplier_name": "Supplier B", "location_id": 2}
        ]
    )
    assert response.status_code == 200
    assert "suppliers created" in response.json()["msg"]

def test_list_suppliers():
    response = client.get("/suppliers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_vehicle():
    response = client.post(
        "/vehicles/", 
        json={"model": "Model X", "prod_date": "2022-01-01", "year": 2022, "propulsion": "electric"}
    )
    assert response.status_code == 200
    assert "model" in response.json()

def test_list_vehicles():
    response = client.get("/vehicles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
