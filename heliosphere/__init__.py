from weppy import App

app = App(__name__)

# Config
app.config.url_default_namespace = "main"

# Language settings
app.languages = ['en', 'it']
app.language_default = 'en'
app.language_force_on_url = True
app.language_write = True

# Extensions
from weppy_haml import Haml
app.config.Haml.set_as_default = True
app.config.Haml.auto_reload = True
app.use_extension(Haml)


# Expose controllers
from controllers import main, api
