from flask import Flask,jsonify,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
  #food = str(Foods[1]['name'])
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True,port=5000)