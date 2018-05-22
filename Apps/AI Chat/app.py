from flask import Flask, render_template, request, url_for, redirect, flash
import os,datetime

app = Flask(__name__)
#app.secret_key = 'secret' #for flash module


@app.route('/', methods=['GET','POST'])
def index():
  msg = str(request.form.get('msg'))
  return render_template('index.html' ,msg=msg)

today = datetime.date.today()

responses = {
  'name':"My name is Rachel",
  'date':'It is ' + today.strftime('%A %B %d, %Y '),
  'birth':"I was born on Tuesday, May 22, 2018",
  'state':"I am feeling okay."
}

@app.route('/submit', methods=['GET','POST'])
def submit():
  msg = str(request.form.get('msg'))
  if msg =='name':
    say(responses['name'])
  elif msg=="date":
    say(responses['date'])
  elif msg=="birth":
    say(responses['birth'])
  elif msg=="state":
    say(responses['state'])
  else:
    say(msg)
  return render_template('index.html',msg=msg)

@app.route('/<endpoint>',methods=['GET','POST'])
def name(endpoint):
  return endpoint

def say(x):
  os.system("say '{}' &".format(x)) #the & allows instant page refresh
  
if __name__ == '__main__':
  app.run(debug=True)