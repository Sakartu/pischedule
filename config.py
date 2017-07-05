import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'tM/5JSQUy&OyYG8)dDFuJ{G?LXR&G}'
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pischedule.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
