from flask import Flask
from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs

app = Flask(__name__)

DEBUG = True


# Flask-FlatPages
flatpages = FlatPages(app)
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
LESSON_DIR = 'lessons'

# Flask-Bootstrap
Bootstrap(app)

# Apply config paramaters (the all-caps variables above)
app.config.from_object(__name__)