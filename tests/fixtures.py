import pytest
from weppy import session

from starter_weppy import app


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
              "Password: {}\n".format(self.email, self.first_name, self.last_name, self.password))


TEST_ADMIN = UserMock('test_admin@example.com',
                      'TestAdminFirst',
                      'TestAdminLast',
                      'testadmin')

TEST_USER = UserMock('test_user@example.com',
                     'TestUserFirst',
                     'TestUserLast',
                     'testuser')


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def logged_client():
    user_client = app.test_client()
    user_client.get("/account/login")
    user_client.post('/account/login', data={
        'email': TEST_USER.email,
        'password': TEST_USER.password,
        '_csrf_token': list(session._csrf)[-1]
    }, follow_redirects=True)
    return user_client
