from weppy import App
from weppy.orm import Database
from weppy.sessions import SessionManager
from weppy.tools.auth import Auth


app = App(__name__, template_folder="./views")

# Config
app.config.url_default_namespace = "main"
app.config.templates_auto_reload = True
app.config.db.adapter = "sqlite"
app.config.db.host = "127.0.0.1"
app.config.auth.single_template = True
app.config.auth.registration_verification = False
app.config.auth.hmac_key = "MassiveDynamicRules"

# Language settings
app.languages = ['en']
app.language_default = 'en'
app.language_force_on_url = True
app.language_write = True

# init database and auth
from starter_weppy.models.user import User

# init auth before passing db models due to dependencies
# on auth tables in the other models
db = Database(app, auto_migrate=True, auto_connect=True)
auth = Auth(app, db, user_model=User)

# adding sessions and authorization handlers
app.pipeline = [
    SessionManager.cookies('Walternate'),
    db.pipe,
    auth.pipe
]


# Extensions
from weppy_haml import Haml
app.config.Haml.set_as_default = True
app.config.Haml.auto_reload = True
app.use_extension(Haml)

auth_routes = auth.module(__name__, url_prefix='account')


# Expose controllers
from starter_weppy.controllers import *

# Commands
from starter_weppy import cli
