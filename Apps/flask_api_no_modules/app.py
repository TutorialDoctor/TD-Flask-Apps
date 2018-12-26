from flask import Flask,request

app = Flask(__name__)
from api import *

if __name__ == "__main__":
    app.run(debug=True,port=5000)



