import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from my_service import MyService
from my_utility import get_service
from my_route import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


@pytest.fixture
def service_mock(mocker):
    mock: MyService = mocker.Mock(spec=MyService)
    mock.get_numbers = mocker.Mock(return_value=[45, 65])
    return mock


@pytest.fixture
def override_dependency(service_mock):
    def get_mock_service():
        return service_mock

    app.dependency_overrides[get_service] = get_mock_service
    try:
        yield
    finally:
        app.dependency_overrides = {}


def test_get_numbers(override_dependency):
    response = client.get("/numbers")
    assert response.status_code == 200
    assert response.json() == {"numbers": [45, 65]}
