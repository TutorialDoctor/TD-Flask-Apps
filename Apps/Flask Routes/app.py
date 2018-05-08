from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Person():
  id = 1
  def __init__(self,name):
    self.id = Person.id
    self.name=name
    Person.id +=1

joe = Person("Joe")
sarah = Person("Sarah")
jane = Person("Jane")
People = [joe,sarah,jane]
  
@app.route('/')
def root():
  return redirect(url_for('index'))

@app.route('/index')
def index():
  people = People
  return render_template("index.html",people=people)

@app.route('/person/new',methods=["GET","POST","DELETE"])
def new():
  if request.method == "POST":
    name =  request.form.get('name')
    new_person = Person(name)
    People.append(new_person)
    return redirect(url_for('index'))
  # DELETE ISNT WORKING RIGHT NOW
  if request.method =="DELETE":
    if new_person.id==1:
      People.remove(new_person)
    return redirect(url_for('index'))
  return render_template("new.html")

@app.route('/person/<int:id>')
def show(id):
  for p in People:
    if p.id == id:
      return render_template('show.html',id=p.id,name=p.name)
  return render_template("show.html",id=id,people=People)

@app.route('/person/<int:id>/edit')
def edit(id):
  for p in People:
    if p.id == id:
      return render_template('edit.html',id=p.id,name=p.name)
  return render_template("edit.html",id=id)

if __name__=="__main__":
  app.run(debug=True, port=5000)