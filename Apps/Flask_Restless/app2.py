from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__)
app.config.from_pyfile('config2.cfg')
db = SQLAlchemy(app)

# Create DB
#@app.before_first_request
#def create_tables():
    #db.create_all() # Create db

class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet',backref='owner',lazy='dynamic')

class Pet(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer,db.ForeignKey('person.id'))

manager = APIManager(app,flask_sqlalchemy_db=db)
manager.create_api(Person,methods=['GET','POST','DELETE','PUT'])
manager.create_api(Pet)


if __name__ =="__main__":
    app.run(debug=True,port=5000)