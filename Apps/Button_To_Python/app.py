from flask import Flask,render_template
import requests

#https://jsonplaceholder.typicode.com

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run():
    message = "Your app is running"
    return render_template("run.html",message=message)

@app.route('/hello')
def hello():
    message = "Hello"
    return render_template("hello.html",message=message)

@app.route('/news')
def news():
    message = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    return render_template("news.html",message=message)

@app.route('/news/<int:id>')
def news_item(id):
    message = requests.get('https://jsonplaceholder.typicode.com/todos/{}'.format(id)).json()
    return render_template("news_item.html",message=message)

if __name__=="__main__":
    app.run(debug=True)
