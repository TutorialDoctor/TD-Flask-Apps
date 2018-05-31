from flask import Flask, render_template,request,redirect,url_for
from faker import Faker
fake = Faker()
# pip install faker

app = Flask(__name__)

db = []

@app.route('/',methods=["GET"])
def index():
  return render_template('index.html',items=str(db))

@app.route('/add',methods=["POST"])
def add():
  new_item = request.form.get('in')
  if new_item != "":
    db.append(new_item)
    return render_template('index.html',new_item=new_item,items=str(db))
  else:
    db.append(fake.name())
    return redirect('/')

@app.route('/delete',methods=["POST"])
def delete():
  del_item = request.form.get('in')
  if del_item in db:
    db.remove(del_item)
    return render_template('index.html',del_item=del_item,items=str(db))
  else: return redirect('/')

@app.route('/clear',methods=["GET"])
def clear():
  global db
  db = []
  return render_template('index.html',items=str(db))

if __name__ == "__main__":
  app.run(debug=True)