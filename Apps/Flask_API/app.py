from flask import Flask,jsonify,render_template,redirect

# A demonstration of how an API works.

app = Flask(__name__)

# Using a dictionary as a Database for proof-of-concept
# This could easily be data in an SQLite database
people_db = [
    {"id":1,"name":"John","age":38,"occupation":"Designer","website":"http://www.deigner.com"},
    {"id":2,"name":"Sarah","age":23,"occupation":"Programmer","website":"http://www.programmer.com"},
    {"id":3,"name":"George","age":61,"occupation":"Civil Engineer","website":"http://www.civilengineer.com"},
    {"id":4,"name":"Henry","age":54,"occupation":"CEO","website":"http://www.ceo.com"},
    {"id":5,"name":"Rebecca","age":12,"occupation":"","website":"http://website.com"},
    ]

# Creating a root endpoint that returns a webpage (index.html) in the templates folder.
@app.route('/')
def index():
    return render_template('index.html')

# Creating an api endpoint that returns the entire database of people as JSON
@app.route('/api/people')
def show_people():
    return jsonify(people_db)

# Creating an api endpoint that returns a person in the people databse with a given id
@app.route('/api/people/<int:id>')
def show_person(id):
    # Try to get a person and return it as json
    try:
        person = people_db[id-1] #-1 because we are actually getting the index
        person_json = jsonify(person)
        return person_json
    # If there is an exception error, display a message that the person they are trying to request doesn't exist
    except:
        return "Person \"{}\" doesn't exist.".format(id)

# Catching URL issues
@app.route('/api')
def slash_api():
    return redirect('/')
@app.route('/<string:name>')
def slash_string(name):
    return redirect('/')
@app.route('/api/<string:name>')
def api_slash_string(name):
    return redirect('/')
@app.route('/api/')
def api_slash():
    return redirect('/')
# End catching URL issues

# Run the app
if __name__=="__main__":
    app.run(debug=True)