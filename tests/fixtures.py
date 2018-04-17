import pytest
from weppy import session

from starter_weppy import app, auth, db
from starter_weppy.dev_utils import (
    setup_admin, remove_admin, setup_user, remove_user)


class UserMock(object):
    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __str__(self):
        print("Email: {}\n"
              "First_Name: {}\n"
              "Last_Name: {}\n"
              "Password: {}\n".format(
              self.email, self.first_name, self.last_name, self.password))


TEST_ADMIN = UserMock('test_admin@example.com',
                      'TestAdminFirst',
                      'TestAdminLast',
                      'testadmin')

TEST_USER = UserMock('test_user@example.com',
                     'TestUserFirst',
                     'TestUserLast',
                     'testuser')


@pytest.fixture(scope='function')
def no_admin_group():
    with db.connection():
        auth.delete_group('admin')
    try:
        with db.connection():
            yield
    finally:
        pass


@pytest.fixture(scope='function')
def client():
    return app.test_client()


@pytest.fixture(scope='function')
def logged_client(request):
    with db.connection():
        setup_user()

        user_client = app.test_client()
        user_client.get("/account/login")
        user_client.post('/account/login', data={
            'email': TEST_USER.email,
            'password': TEST_USER.password,
            '_csrf_token': list(session._csrf)[-1]
        }, follow_redirects=True)

    try:
        with db.connection():
            yield user_client
    finally:
        with db.connection():
            remove_user()


@pytest.fixture(scope='function')
def admin_client(request):
    with db.connection():
        setup_admin()

        admin_client = app.test_client()
        admin_client.get("/account/login")
        admin_client.post('/account/login', data={
            'email': TEST_ADMIN.email,
            'password': TEST_ADMIN.password,
            '_csrf_token': list(session._csrf)[-1]
        }, follow_redirects=True)

    try:
        with db.connection():
            yield admin_client
    finally:
        with db.connection():
            remove_admin()
