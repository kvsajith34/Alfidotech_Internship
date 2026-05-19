import pytest
import json
import sys
import os
sys.path.insert(0, os.path.abspath("."))

from app.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Home endpoint must return 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_health_endpoint(client):
    """Health endpoint must return healthy"""
    response = client.get("/health")
    data = json.loads(response.data)
    assert data["status"] == "healthy"

def test_predict_endpoint(client):
    """Predict endpoint must return valid class"""
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    response = client.post(
        "/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )
    data = json.loads(response.data)
    assert "prediction" in data
    assert data["prediction"] in ["setosa", "versicolor", "virginica"]
    assert "confidence" in data

def test_predict_invalid_input(client):
    """Predict endpoint must handle bad input"""
    response = client.post(
        "/predict",
        data=json.dumps({"wrong": "data"}),
        content_type="application/json"
    )
    assert response.status_code == 400
