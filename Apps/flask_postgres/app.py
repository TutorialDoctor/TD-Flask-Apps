from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

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
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    #id = db.Column(db.Integer)
    name = db.Column(db.String(120), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<E-mail %r>' % self.name


@app.route('/')
def index(): 
  users = User.query.all()
  return render_template('index.html',users=users)

@app.route('/prereg', methods=['POST'])
def prereg():
    #name = None
    if request.method == 'POST':
        name = request.form['name']
        #name='joe'
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.name == name).count():
            reg = User(name)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html',name=name)
    return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)