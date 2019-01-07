from app import app
import requests
from flask import jsonify

#FRONTEND CODE GOES HERE
@app.route('/')
def index():
    return "Hello Application"

@app.route('/controllers') #go here
def controllers():
  api_token = ""
  headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(api_token)}
  r = requests.get('http://localhost:5000/api/v1/controller1', headers=headers)
  data = r.json() # THIS WORKS!
  return jsonify(data)
  #return render_template('index.html',services=services)
