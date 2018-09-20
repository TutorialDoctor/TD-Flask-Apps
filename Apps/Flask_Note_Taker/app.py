from flask import Flask,jsonify,url_for,render_template,request
from faker import Faker

app = Flask(__name__)

database = [
  {'people':[
    {'name':'Joe'},
    {'name':'Sarah'},
    {'name':'Henry'},
    {'name':'Bella'},
    {'name':'George'},
    {'name':'Valerie'},
]}
]

#this database isn't persistent but is good for testing. I will eventually use Sqlite. Postgresql is better once set up.

@app.route('/')
def index():
  #food = str(Foods[1]['name'])
  return render_template('index.html')

@app.route('/show',methods=['post'])
def show():
  title = request.form.get('title')
  text = request.form.get('text')
  with open('documents/'+title+".txt",'w') as outfile:
    outfile.write(text)
  return render_template('view_templates/show.html',title=title,text=text)


# CREATE
@app.route('/create',methods=['get','post'])
def create():
  with open('documents/new.txt','w') as outfile:
    outfile.write("You created a new file.")
  return "Created a new file: \"new.txt\""

# READ
@app.route('/read/<int:id>',methods=['get'])
def read(id):
    return jsonify(database[0]['people'][id]['name']+' '+str(id))

# UPDATE
@app.route('/update',methods=['get','put'])
def update():
  return "Update Something"

# DELETE
@app.route('/delete',methods=['get','delete'])
def delete():
  return "Delete Something"


if __name__ == '__main__':
  app.run(debug=True,port=5000)