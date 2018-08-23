from flask import Flask,jsonify,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
  #food = str(Foods[1]['name'])
  return render_template('index.html')

@app.route('/show',methods=['post'])
def test():
  email = request.form.get('email')
  example = request.form.get('example')
  selection = request.form.get('selection')
  text = request.form.get('text')
  return render_template('app_templates/show.html',selection=selection,email=email,text=text,example=example)

if __name__ == '__main__':
  app.run(debug=True,port=5000)