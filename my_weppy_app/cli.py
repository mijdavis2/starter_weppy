"""
Usage:   weppy --app=my_weppy_app <command>
Example: weppy --app=my_weppy_app shell
"""
from my_weppy_app import app


@app.cli.command('routes')
def print_routing():
    print app.route.routes_out


@app.cli.command('get_users')
def print_users():
    from my_weppy_app import db
    from my_weppy_app.models.user import User
    rows = db(User.email).select()
    for row in rows:
        print row
