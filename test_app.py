import pytest
from app import app, load_and_split_pdf

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_greetings(client):
    response = client.post('/chat', json={'prompt': 'Oi'})
    assert b'Olá!' in response.data

def test_pdf_loading():
    try:
        load_and_split_pdf()
        assert True
    except Exception:
        assert False