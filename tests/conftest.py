import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Provide a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def sample_activity():
    """Provide sample activity data for testing."""
    return {
        "name": "Test Activity",
        "description": "A test activity",
        "schedule": "Mondays, 3:00 PM - 4:00 PM",
        "max_participants": 10,
        "participants": ["test1@example.com", "test2@example.com"]
    }
