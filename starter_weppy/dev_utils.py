from starter_weppy import db
from tests.fixtures import *


def setup_dev_users():
    admin = db.User.validate_and_insert(
            email=TEST_ADMIN.email,
            first_name=TEST_ADMIN.first_name,
            last_name=TEST_ADMIN.last_name,
            password=TEST_ADMIN.password
    )
    user = db.User.validate_and_insert(
            email=TEST_USER.email,
            first_name=TEST_USER.first_name,
            last_name=TEST_USER.last_name,
            password=TEST_USER.password
    )
    db.commit()
    print("Admin: {}\n"
          "User: {}\n".format(admin.__dict__, user.__dict__))


def remove_dev_users():
    from starter_weppy.models.user import User
    from tests.fixtures import TEST_ADMIN, TEST_USER
    print(db(User.email == TEST_ADMIN.email).select())
    print(db(User.email == TEST_USER.email).select())
    db(User.email == TEST_ADMIN.email).delete()
    db(User.email == TEST_USER.email).delete()
    db.commit()
