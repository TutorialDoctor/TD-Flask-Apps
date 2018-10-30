from app.setup import app,db
#from ..controllers.users import *


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable= False)
    birth_date = db.Column(db.DATE)
    age = db.Column(db.VARCHAR(16))
    gender = db.Column(db.String(6))
    email = db.Column(db.VARCHAR(255), unique=True)
    website = db.Column(db.VARCHAR(255))
    alive = db.Column(db.VARCHAR(6))
    created_at = db.Column(db.TIMESTAMP)

    def __init__(self, first_name,last_name,birth_date,age,gender,email,website,alive,created_at):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.age = age
        self.gender = gender
        self.email = email
        self.website = website
        self.alive = alive
        self.created_at = created_at

    def __repr__(self):
        return '<E-mail %r>' % self.first_name