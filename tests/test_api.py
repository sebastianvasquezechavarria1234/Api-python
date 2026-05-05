import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_triangulo_endpoint_success(client):
    response = client.post('/api/triangulo', json={
        "base": 3,
        "altura": 4,
        "lado1": 4,
        "lado2": 5
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['data']['area'] == 6.0
    assert data['data']['perimetro'] == 12.0

def test_triangulo_endpoint_invalid_triangle(client):
    response = client.post('/api/triangulo', json={
        "base": 100,
        "altura": 10,
        "lado1": 1,
        "lado2": 1
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "form a valid triangle" in data['error']

def test_triangulo_endpoint_missing_field(client):
    response = client.post('/api/triangulo', json={
        "base": 10,
        "altura": 5
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "Missing required field" in data['error']
