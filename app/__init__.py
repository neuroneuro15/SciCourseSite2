from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Flask-SQLAchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/testflask.db'
db = SQLAlchemy(app)

# Flask-Bootstrap
Bootstrap(app)
