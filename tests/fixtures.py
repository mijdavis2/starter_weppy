class TestUser(object):
    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __str__(self):
        print "Email: {}\n" \
              "First_Name: {}\n" \
              "Last_Name: {}\n" \
              "Password: {}\n".format(self.email, self.first_name, self.last_name, self.password)


TEST_ADMIN = TestUser('test_admin@example.com',
                      'TestAdminFirst',
                      'TestAdminLast',
                      'testadmin')

TEST_USER = TestUser('test_user@example.com',
                      'TestUserFirst',
                      'TestUserLast',
                      'testuser')
