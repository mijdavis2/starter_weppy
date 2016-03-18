import pytest
from heliosphere import app


@pytest.fixture()
def client():
    return app.test_client()


def test_welcome(client):
    resp = client.get('/')
    assert 'Welcome to the Heliosphere' in resp.data


def test_error_404(client):
    resp = client.get('asidufhlaksdjfliasghdlk')
    assert "<title>Helio-404</title>" in resp.data
