from flask import Flask

# adding database
import os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# from models import Test
