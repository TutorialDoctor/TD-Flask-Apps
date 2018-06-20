from flask import Flask, request,jsonify

#https://github.com/PrettyPrinted/bottle_restful_api

app = Flask(__name__)

animals = [{'name' : 'Ellie', 'type' : 'Elephant'},
			{'name' : 'Python', 'type' : 'Snake'},
			{'name' : 'Zed', 'type' : 'Zebra'}]

@app.route('/')
def index():
	return '<h1>Animals</h1>'
  
@app.route('/animal')
def getAll():
	return jsonify({'animals' : animals})

@app.route('/animal/<name>')
def getOne(name):
	the_animal = [animal for animal in animals if animal['name'] == name]
	return jsonify({'animal' : the_animal[0]})

@app.route('/animal',methods=['post'])
def addOne():
	new_animal = {'name' : request.json['name'], 'type' : request.json['type']}
	animals.append(new_animal)
	return jsonify({'animals' : animals})

@app.route('/animal/<name>',methods=['delete'])
def removeOne(name):
	the_animal = [animal for animal in animals if animal['name'] == name]
	animals.remove(the_animal[0])
	return jsonify({'animals' : animals})

if __name__=='__main__':
  app.run(debug=True)