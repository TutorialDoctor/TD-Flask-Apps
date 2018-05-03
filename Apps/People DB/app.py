from flask import Flask, render_template, request, g, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
import sqlite3
        
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class People(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String(50))
  lastName = db.Column(db.String(50))
  middleInitial = db.Column(db.String(1))
  age = db.Column(db.Integer())
  sex = db.Column(db.String(1))
  address = db.Column(db.String(50))
  comment = db.Column(db.String(1000))

  
@app.route("/")
def index():
  hello = "Hello, Pierre"
  people = People.query.all()
  return render_template('index.html', people=people, hello=hello)

@app.route("/create")
def create():
  return render_template('people.html')

@app.route('/process', methods=['POST'])
def process():
  firstname = request.form['firstName']
  lastname = request.form['lastName']
  middleInitial = request.form['middleInitial']
  age = request.form['age']
  sex = request.form['sex']
  address = request.form['address']
  comment = request.form['comment']
  info = People(firstName=firstname, lastName=lastname,middleInitial=middleInitial,age=age,sex=sex,address=address,comment=comment)
  db.session.add(info)
  db.session.commit()
  return redirect(url_for('index'))

if __name__=='__main__':
  app.run(debug=True)
