# test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Provide your valid contact details.' in response.data

def test_form_submission(client):
    response = client.post('/', data={
        'first_name': 'John',
        'last_name': 'Doe',
        'contact_no': '1234567890',
        'email': 'john@example.com',
        'username': 'johndoe',
        'password': 'password123'
    })
    
    if response.status_code == 200 or response.status_code == 204:
        assert b'Form submitted successfully!' in response.data
        assert "form submitted"
    elif response.status_code == 500:
        assert "internal server issue" in response.data
