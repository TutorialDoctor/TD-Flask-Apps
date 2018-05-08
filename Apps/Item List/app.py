from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

# 1. Create a new app
# 2. Configure the database
# 3. Create a SQL datbase object
# 4. In folder "from app import db" then "db.create_all()" to create database with Item table
# 5. http://5000 in browser.


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20))

@app.route('/')
def index():
  #all_items = Item.query.order_by('name desc').all()
  all_items = Item.query.all()
  return render_template("index.html",all=all_items)

@app.route('/new', methods=['POST'])
def new():
  name = request.form['name']
  new_item = Item(name=name)
  db.session.add(new_item)
  db.session.commit()
  return redirect(url_for('index'))
    
if __name__=="__main__":
  app.run(debug=True)
  
