from flask import Flask, render_template, request, g, redirect, url_for
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
import sqlite3
from datetime import datetime

#from app.py import db
# db.create_all()
#2016-01-01 10:20:05.123
LIMIT = 30

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Bootstrap(app)

class Trainee(db.Model):
  __tablename__='trainee'
  id = db.Column(db.Integer, primary_key=True)
  name =  db.Column(db.String(50))
  date = db.Column(db.DateTime)
  weight = db.Column(db.Integer)
  height = db.Column(db.Integer)
  comment = db.Column(db.String(1000))
  #the trainer_id is an integer column with a foreign key of the trainer id
  trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))

class Trainer(db.Model):
  __tablename__='trainer'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  # this trainer has a relationship with the Trainees model and a backreference of "trainer"
  trainee = db.relationship('Trainee', backref='trainer')
  
@app.route("/")
def index():
  hello_text = "Trainees"
  result = Trainee.query.order_by('name desc').limit(LIMIT).all()
  return render_template('index.html', result=result)
  #return render_template('index.html')

@app.route("/new")
def new():
  login_text = "You've logged in successfully!"
  return render_template("new.html",login_text=login_text)

@app.route("/login")
def login():
  login_text = "You've logged in successfully!"
  return render_template("login.html",login_text=login_text)

@app.route('/process', methods=['POST'])
def process():
  name = request.form['name']
  date = datetime.now()
  weight = request.form['weight']
  height = request.form['height']
  comment = request.form['comment']
  trainer = Trainer(name=request.form['trainer'])
  signature = Trainee(name=name,date=date,weight=weight,height=height,comment=comment,trainer=trainer)
  db.session.add(signature)
  db.session.commit()
  db.session.add(trainer)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/delete',methods=['DELETE'])
def delete():
  signature = Trainees(name=name,date=date,weight=weight,height=height,comment=comment,trainer=trainer)
  db.session.delete(sig)
  db.sessioin.commit
  return redirect(url_for('index'))

@app.route("/eating")
def eating():
  return render_template('pages/eating.html')

@app.route("/workout")
def workout():
  return render_template('pages/workout.html')

@app.route("/resting")
def resting():
  return render_template('pages/resting.html')

@app.route('/delete/<int:entry_id>')
def delete_entry(entry_id):
  g.db.execute('delete from entries where id=' + entry_id)

if __name__=='__main__':
  app.run(debug=True)
  