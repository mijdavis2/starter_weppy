"""
Usage:   weppy --app=heliosphere <command>
Example: weppy --app=heliosphere shell
"""
from heliosphere import app


@app.cli.command('routes')
def print_routing():
    print app.route.routes_out
