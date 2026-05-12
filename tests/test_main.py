import pytest
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from main import app

client = TestClient(app)


def test_health_check_status_code():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_check_response_body():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_health_check_content_type():
    response = client.get("/health")
    assert response.headers["content-type"] == "application/json"


def test_unknown_route_returns_404():
    response = client.get("/nonexistent")
    assert response.status_code == 404
