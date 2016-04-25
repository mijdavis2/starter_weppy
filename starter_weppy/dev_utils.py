from starter_weppy import db, auth
from tests.fixtures import *


def setup_dev_users():
    dev_admin = _setup_admin()
    dev_user = _setup_user()
    print("Admin: {} \nUser: {}\n".format(dev_admin.as_dict(), dev_user.as_dict()))


def remove_dev_users():
    print("\nRemoving dev admin and user.")
    from starter_weppy.models.user import User
    from tests.fixtures import TEST_ADMIN, TEST_USER
    dev_admin = db(User.email == TEST_ADMIN.email).select()
    dev_user = db(User.email == TEST_USER.email).select()
    print("Admin: {} \nUser: {}\n".format(dev_admin.as_dict(), dev_user.as_dict()))
    db(User.email == TEST_ADMIN.email).delete()
    db(User.email == TEST_USER.email).delete()
    print("Dev admin and user successfully deleted.")
    db.commit()


def _setup_admin():
    admin = db.User.validate_and_insert(
            email=TEST_ADMIN.email,
            first_name=TEST_ADMIN.first_name,
            last_name=TEST_ADMIN.last_name,
            password=TEST_ADMIN.password
    )
    # Create admin group if id doesn't exist.
    admins = auth.id_group("admin")
    if not admins:
        auth.add_group("admin")
    auth.add_membership(admins, admin.id)
    db.commit()
    return admin


def _setup_user():
    user = db.User.validate_and_insert(
            email=TEST_USER.email,
            first_name=TEST_USER.first_name,
            last_name=TEST_USER.last_name,
            password=TEST_USER.password
    )
    db.commit()
    return user
