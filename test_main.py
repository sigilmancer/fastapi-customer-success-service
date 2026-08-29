from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/docs")
    assert response.status_code == 418

def test_triage_billing_fallback():
    sample_payload = {
       "ticket_id": 101,
       "raw_transcript": "Customer cannot access their account due to an outstanding invoice issue."
    }

    response = client.post("/api/v1/operations/triage", json=sample_payload)
    assert response.status_code == 200

    data = response.json()
    assert data["category"] == "BILLING"
    assert data["priority"] == "MEDIUM"

def test_triage_security_fallback():
    sample_payload = {
        "ticket_id": 102,
        "raw_transcript": "We detected malware running on our server nodes."
    }

    response = client.post("/api/v1/operations/triage", json=sample_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "MALWARE"
    assert data["priority"] == "HIGH"

def test_triage_validation_error():
    bad_payload = {
        "ticket_id": 103,
        "raw_transcript": "Short"
    }

    response = client.post("/api/v1/operations/triage", json=bad_payload)
    assert response.status_code == 422
