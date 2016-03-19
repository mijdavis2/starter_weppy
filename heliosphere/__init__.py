from weppy import App, DAL
from weppy.sessions import SessionCookieManager
from weppy.tools import Auth

app = App(__name__)

# Config
app.config.url_default_namespace = "main"

# Language settings
app.languages = ['en']
app.language_default = 'en'
app.language_force_on_url = True
app.language_write = True

# init database and auth
from models.user import User

# init auth before passing db models due to dependencies
# on auth tables in the other models
db = DAL(app)
auth = Auth(
        app, db, usermodel=User, base_url="account"
)

# adding sessions and authorization handlers
app.route.common_handlers = [
    SessionCookieManager('verySecretKey'),
    db.handler,
    auth.handler
]

# Extensions
from weppy_haml import Haml
app.config.Haml.set_as_default = True
app.config.Haml.auto_reload = True
app.use_extension(Haml)

# Expose controllers
from controllers import main, api


# Commands
import cli