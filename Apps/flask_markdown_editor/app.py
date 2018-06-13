from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

READ= 'r'
WRITE='w'
APPEND = 'a'
UNIVERSAL = 'U'
UNIVERSAL_READLINE = 'rU'

@app.route('/',methods=['GET','POST'])
def index():
  with open('files/programming.txt',READ) as infile:
    text = infile.read()
  data = text
  return render_template('index.html',exports=str(data))

@app.route('/text')
def text():
  data = text
  return render_template('text.html',text=data)

@app.route('/sum',methods=['GET','POST'])
def summ():
  num1 = request.form.get('num1')
  num2 = request.form.get('num2')
  summ = str(int(num1)+int(num2))
  return render_template('sum.html',summ=summ)

if __name__ == "__main__":
  app.run(debug=True)