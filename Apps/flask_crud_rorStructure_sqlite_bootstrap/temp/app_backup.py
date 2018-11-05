from flask import Flask,request,json,render_template
from flask_sqlalchemy import SQLAlchemy
#from models.users import User,db
#from controllers import Controllers
from faker import Faker
import random

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
      
@app.route('/')
def index(): 
  users = User.query.all()
  return render_template('index.html',users=users)

@app.route('/prereg', methods=['POST'])
def prereg():
    #name = None
    if request.method == 'POST':
        try:
          first_name = request.form['first_name']
          last_name= request.form['last_name']
          birth_date = request.form['birth_date']
          age = request.form['age']
          gender = request.form['gender']
          email = request.form['email']
          website = request.form['website']
          alive = request.form['alive']
          created_at = request.form['created_at']
        except:
          first_name = fake.first_name()
          last_name= fake.last_name()
          birth_date = fake.date()
          age = str(random.randint(18,65))
          gender = "Male"
          email = fake.email()
          website = fake.url()
          alive = ["true",'false']
          alive = alive[random.randint(0,1)]
          created_at = "2001-09-28 01:00:00"
        #name='joe'
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.first_name == first_name).count():
            reg = User(first_name,last_name,birth_date,age,gender,email,website,alive,created_at)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html',first_name=first_name)
    return render_template('index.html')
  

if __name__ == "__main__":
  app.run(debug=True)