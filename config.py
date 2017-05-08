__author__ = 'Maru'

import os

dbhost = 'localhost:3306'
dbuser = 'root'
dbpass = ''
dbname = 'iCCUT'
DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' +dbname

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
