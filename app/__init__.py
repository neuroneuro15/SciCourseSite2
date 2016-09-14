from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Flask-SQLAchemy
# import os
# if os.path.isfile(r'/tmp/testflask.db'):
#     os.remove(r'/tmp/testflask.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/testflask.db'
db = SQLAlchemy(app)

# Flask-Bootstrap
Bootstrap(app)
