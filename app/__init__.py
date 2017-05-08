__author__ = 'Maru'

import sys
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key=os.urandom(24)
app.config.from_object("config")
db = SQLAlchemy(app)

from app import views,models