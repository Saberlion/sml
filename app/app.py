# -*- coding:utf8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('hello.cfg')

db = SQLAlchemy(app)
from API.api import api_module
app.register_blueprint(api_module)