from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config.from_object('config')
if not app.config.get('SECRET_KEY', ''):
    print('SECRET_KEY is empty, please generate one by starting a python console, then run:\n>>> import os\n>>> os.urandom(24)\nand paste the resulting string in config.py as a value for SECRET_KEY.')
    sys.exit(-1)

db = SQLAlchemy(app)

from app import views, models, filters
