from starter_weppy import User, db
from starter_weppy import utils
from tests.fixtures import (
    client, admin_client, logged_client, no_admin_group, TEST_USER)


def test_welcome_page_access(client):
    resp = client.get('/')
    assert 'Welcome to StarterWeppy' in resp.data


def test_error_404(client):
    resp = client.get(utils.get_cryptogen_string())
    assert "<title>StarterWeppy-404</title>" in resp.data


def test_account_page_access(client):
    resp = client.get('/account/login')
    assert "StarterWeppy | Login" in resp.data


def test_users_page_access(client):
    resp = client.get('/users')
    assert "StarterWeppy-403" in resp.data


def test_admin_users_page_access(admin_client):
    resp = admin_client.get('/users')
    assert "StarterWeppy | Users" in resp.data


def test_admin_users_page_access_wo_admin_group(no_admin_group, admin_client):
    resp = admin_client.get('/users')
    assert "StarterWeppy | Users" in resp.data


def test_profile_page(logged_client):
    resp = logged_client.get('/account/profile')
    assert 'StarterWeppy | Profile' in resp.data


def test_self_user_page(logged_client):
    rows = db(User.email == TEST_USER.email).select()
    test_user_id = rows[0].id
    resp = logged_client.get('/user/{}'.format(test_user_id))
    assert TEST_USER.first_name in resp.data
    assert TEST_USER.last_name in resp.data


def test_maintenance_page(client):
    resp = client.get("/maintenance_check")
    assert "StarterWeppy | Maintenance" in resp.data
