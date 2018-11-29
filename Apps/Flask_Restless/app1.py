from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

app = Flask(__name__)
app.config.from_pyfile('config1.cfg')
db = SQLAlchemy(app)

# Create DB
@app.before_first_request
def create_tables():
    db.create_all() # Create db

class Parent(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    children = db.relationship('Child',backref='parent',lazy='dynamic')

class Child(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    parent_id = db.Column(db.Integer,db.ForeignKey('parent.id'))

manager = APIManager(app,flask_sqlalchemy_db=db)
manager.create_api(Parent,methods=['GET','POST','DELETE','PUT'])
manager.create_api(Child)


if __name__ =="__main__":
    app.run(debug=True,port=5000)

