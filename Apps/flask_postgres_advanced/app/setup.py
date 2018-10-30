from flask import Flask,request,json,render_template
from flask_sqlalchemy import SQLAlchemy
import random
from faker import Faker

app = Flask(__name__)
fake = Faker()

POSTGRES = {
    'user': '',
    'pw': '',
    'db': 'sample_db',
    'host': 'localhost',
    'port': '5433',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)

from .controllers.users import *
from .models.User import User