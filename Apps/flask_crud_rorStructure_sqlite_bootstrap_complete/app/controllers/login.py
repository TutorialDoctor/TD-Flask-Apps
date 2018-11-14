from app.setup import app,db,render_template,request,random,fake
from datetime import datetime

@app.route('/login')
def login(): 
  return render_template('components/login.html')