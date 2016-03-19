import pytest
from heliosphere import app, db


@pytest.fixture()
def client():
    return app.test_client()


def test_welcome_page_access(client):
    resp = client.get('/')
    assert 'Welcome to the Heliosphere' in resp.data


def test_error_404(client):
    resp = client.get('asidufhlaksdjfliasghdlk')
    assert "<title>Heliosphere-404</title>" in resp.data


def test_account_page_access(client):
    resp = client.get('/account/login')
    assert "Heliosphere | Account" in resp.data


def test_users_page_access(client):
    resp = client.get('/users/')
    assert "Heliosphere | Users" in resp.data


@pytest.fixture()
def logged_client(client):
    resp = client.get('/account/login')
    client.post('/account/login', data={
        'email': 'mdavis@sungevity.com',
        'password': 'sungevity',
        '_csrf_token': list(resp.context.session._csrf)[-1]
    }, follow_redirects=True)
    return client


def test_login_page(logged_client):
    resp = logged_client.get('/account/profile')
    assert 'Profile' in resp.data


def test_profile_page(logged_client):
    # how do I get the current_user id?
    current_user_id = 1
    resp = logged_client.get('/user/{}'.format(current_user_id))
    assert "Michael Davis" in resp.data
