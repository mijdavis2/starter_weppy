from weppy import response
from weppy import url, redirect

from starter_weppy import app, auth, auth_routes


@app.route("/")
def welcome():
    response.meta.title = "StarterWeppy"
    return dict()


@auth_routes.after_login
def after_login(form):
    redirect(url('welcome'))
