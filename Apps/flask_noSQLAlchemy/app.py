# all the imports
import sqlite3
from flask import Flask
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
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  cur.execute("INSERT INTO account_holder (email,username,phone,password) VALUES (?,?,?,?)", (email,username,phone,password))
  con.commit()
  con.close()

def insert_contact(name,phone,username,email):
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  cur.execute("INSERT INTO contact (name,phone,username,email) VALUES (?,?,?,?)", (name,phone,username,email))
  con.commit()
  con.close()

def select_account_holder(params=()):
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  result = cur.execute("select * from account_holder")
  con.close()
  return result
          
def select_contact(params=()):
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  result = cur.execute("select * from contact")
  return result.fetchall()
  con.close()
          
@app.route('/')
def index():
  con = sqlite3.connect("database.db")
  cur = con.cursor()
  insert_contact('tutorial','111-111-1111','tutorialdoctor','thetutorialdoctor@gmail.com')
  return str(select_contact(('tutorial','111-111-1111','tutorialdoctor','thetutorialdoctor@gmail.com')))
  con.close()

if __name__ == '__main__':
    init_db()
    app.run()
