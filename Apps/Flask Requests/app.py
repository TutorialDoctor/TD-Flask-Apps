from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = 'secret'

class Person():
  id = 1
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.id = Person.id
    Person.id+=1

joe = Person('Joe',24)
People = [joe]

@app.route('/', methods=['GET','POST'])
def index():
  name = str(request.form.get('name'))
  age = str(request.form.get('age'))
  return render_template('index.html' ,name=name,age=age)

@app.route('/<endpoint>',methods=['GET','POST'])
def name(endpoint):
  return endpoint

@app.route('/submit', methods=['GET','POST'])
def submit():
  name = str(request.form.get('name'))
  age = str(request.form.get('age'))
  new_person = Person(name,age)
  if new_person not in People:#this may be unnecessary
    if name !='' and age !='':
      People.append(new_person)
      #flash("Successfully created person!")
      return render_template('index.html',people=People)
  return render_template('index.html',people=People)
  
if __name__ == '__main__':
  app.run(debug=True)