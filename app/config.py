from os import path, urandom

basedir = path.abspath(path.dirname(__file__))
dbname = "dbname.db"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, dbname)
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

#DEBUG = True
TESTING = True
SECRET_KEY = urandom(30)
