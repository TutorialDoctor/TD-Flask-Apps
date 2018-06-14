# all the imports
import sqlite3
from flask import Flask,render_template,request,redirect
from contextlib import closing

#First, I ran 'sqlite3 database.db < schema.sql' from the terminal to generate the database.db file from the schema file.

# configuration
DATABASE = './database.db'
DEBUG = True


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def insert_account_holder(email,username,phone,password):
  con = sqlite3.connect("database.db",timeout=10)
  cur = con.cursor()
  cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)", (email,username,phone,password))
  con.commit()
  con.close()

def insert_contact(name,phone,username,email):
  con = sqlite3.connect("database.db",timeout=10)
  cur = con.cursor()
  cur.execute("INSERT INTO contact (name,phone,username,email) VALUES (?,?,?,?)", (name,phone,username,email))
  con.commit()
  con.close()

def select_account_holder(params=()):
  con = sqlite3.connect("database.db",timeout=10)
  cur = con.cursor()
  result = cur.execute("select * from account_holder")
  con.close()
  return result
          
def select_contact(params=()):
  con = sqlite3.connect("database.db",timeout=10)
  cur = con.cursor()
  result = cur.execute("select * from contact")
  return result.fetchall()
  con.close()
          
@app.route('/')
def index():
  con = sqlite3.connect("database.db",timeout=10)
  cur = con.cursor()
  every_contact = cur.execute('select * from contact')
  result_contacts = every_contact.fetchall()
  every_account = cur.execute('select * from account_holder')
  result_accounts = every_account.fetchall()
  return render_template('index.html',every_contact=result_contacts)
  con.close()
  
@app.route('/newcontact')
def new_contact():
  return render_template('newcontact.html')

@app.route('/newaccount')
def new_account():
  return render_template('newaccount.html')
  
@app.route('/submitcontact',methods=["POST","GET"])
def submit_contact():
  con = sqlite3.connect("database.db",timeout=10)
  cur = con.cursor()
  name= request.form.get('name')
  phone=request.form.get('phone')
  username=request.form.get('username')
  email=request.form.get('email')
  insert_contact(name,phone,username,email)
  every_contact = cur.execute('select * from contact')
  result_contacts = every_contact.fetchall()
  con.commit()
  return render_template('index.html',name=name,phone=phone,username=username,email=email,every_contact=result_contacts)
  con.close()

@app.route('/submitaccount',methods=["POST","GET"])
def submit_account():
  con = sqlite3.connect("database.db",timeout=10)
  cur = con.cursor()
  email=request.form.get('email')
  username=request.form.get('username')
  phone=request.form.get('phone')
  password= request.form.get('password')
  insert_account_holder(email,username,phone,password)
  every_account = cur.execute('select * from account_holder')
  result_accounts = every_account.fetchall()
  con.commit()
  return render_template('index.html',email=email,username=username,phone=phone,password=password,every_account=result_accounts)
  con.close()

  
if __name__ == '__main__':
    init_db()
    app.run()
