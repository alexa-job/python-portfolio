from main import app
from fastapi.testclient import TestClient

client = TestClient(app) # передаем приложение

def test_weather ():
    response = client.get("/weather/Москва") # имитируем запрос
    data = response.json()
    assert response.status_code == 200
    assert "city" in data
    assert "temperature" in data
    assert "wind" in data
    assert "rain" in data    