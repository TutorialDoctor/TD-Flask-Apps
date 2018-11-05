from app.setup import app,db,render_template,request,random,fake
from ..models.User import *
from datetime import datetime

@app.route('/')
def user_index(): 
  users = User.query.all()
  return render_template('users/index.html',users=users)

@app.route('/user/add', methods=['POST'])
def create_user():
    if request.method == 'POST':
        try:
          first_name = request.form['first_name']
          last_name= request.form['last_name']
          #birth_date = request.form['birth_date'] #must be converted to date
          birth_date = datetime(2018,9,28,10,10,10).date()
          #birth_date = fake.date()
          #birth_date= datetime(2018,9,28,10,10,10).date()
          age = request.form['age']
          gender = request.form['gender']
          email = request.form['email']
          website = request.form['website']
          alive = request.form['alive']
          #created_at = request.form['created_at']
          created_at = datetime(2018,9,28,10,10,10)
          #created_at = datetime(2018,9,28,10,10,10).strftime("%Y-%m-%d %H:%M:%S")
          #created_at = datetime.now()
        except:
          first_name = fake.first_name()
          last_name= fake.last_name()
          #birth_date = fake.date() #must be converted to date
          birth_date = datetime(2018,9,28,10,10,10).date()
          age = str(random.randint(18,65))
          gender = "Male"
          email = fake.email()
          website = fake.url()
          alive = ["true",'false']
          alive = alive[random.randint(0,1)]
          created_at = datetime(2018,9,28,10,10,10)
          #created_at = datetime(2018,9,28,10,10,10).strftime("%Y-%m-%d %H:%M:%S")
          #created_at = datetime.now()
        #name='joe'
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.first_name == first_name).count():
            reg = User(first_name,last_name,birth_date,age,gender,email,website,alive,created_at)
            db.session.add(reg)
            db.session.commit()
            return render_template('users/success.html',first_name=first_name)
    return render_template('users/index.html')