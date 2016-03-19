from weppy import response
from heliosphere import app, auth


@app.on_error(404)
def error_404():
    response.meta.title = "Heliosphere-404"
    return app.render_template("404.haml")


@app.route("/")
def welcome():
    response.meta.title = "Heliosphere"
    return dict()


@app.route('/account(/<str:f>)?(/<str:k>)?')
def account(f, k):
    response.meta.title = "Heliosphere | Account"
    form = auth(f, k)
    return dict(req=f, form=form)
