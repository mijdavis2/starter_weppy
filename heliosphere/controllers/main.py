from weppy import response
from heliosphere import app


@app.on_error(404)
def error_404():
    response.meta.title = "Helio-404"
    return app.render_template("404.haml")


@app.route("/")
def welcome():
    response.meta.title = "Heliosphere"
    return dict()
