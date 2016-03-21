import pytest
from my_weppy_app import app, db, User
from my_weppy_app import utils
from tests.fixtures import TEST_USER


@pytest.fixture()
def client():
    return app.test_client()


def test_welcome_page_access(client):
    resp = client.get('/')
    assert 'Welcome to MyWeppyApp' in resp.data


def test_error_404(client):
    resp = client.get(utils.get_cryptogen_string())
    assert "<title>MyWeppyApp-404</title>" in resp.data


def test_account_page_access(client):
    resp = client.get('/account/login')
    assert "MyWeppyApp | Account" in resp.data


def test_users_page_access(client):
    resp = client.get('/users/')
    assert "MyWeppyApp | Users" in resp.data


@pytest.fixture()
def logged_client(client):
    resp = client.get('/account/login')
    client.post('/account/login', data={
        'email': TEST_USER.email,
        'password': TEST_USER.password,
        '_csrf_token': list(resp.context.session._csrf)[-1]
    }, follow_redirects=True)
    return client


def test_login_page(logged_client):
    resp = logged_client.get('/account/profile')
    assert 'Profile' in resp.data


def test_profile_page(logged_client):
    db._adapter.reconnect()
    rows = db(User.email == TEST_USER.email).select()
    test_user_id = rows[0].id
    resp = logged_client.get('/user/{}'.format(test_user_id))
    assert TEST_USER.first_name in resp.data
    assert TEST_USER.last_name in resp.data
