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

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
#%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_posts.db'
db = SQLAlchemy(app)
#db.create_all()

from .controllers.users import *
from .models.User import User
from .models.Post import Post
from .controllers.posts import *