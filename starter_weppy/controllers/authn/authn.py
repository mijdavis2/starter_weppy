from starter_weppy import auth, auth_routes
from weppy import response, url, redirect


@auth_routes.login()
def login():
    if auth.is_logged():
        redirect(url('auth.profile'))
    response.meta.title = "StarterWeppy | Login"
    return auth_routes._login()


@auth_routes.profile()
def profile():
    response.meta.title = "StarterWeppy | Profile"
    return auth_routes._profile()


@auth_routes.after_login
def after_login(form):
    redirect(url('welcome'))
