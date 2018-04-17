from weppy import response
from weppy import url, redirect

from starter_weppy import app


@app.route("/")
def welcome():
    response.meta.title = "StarterWeppy"
    return dict()
