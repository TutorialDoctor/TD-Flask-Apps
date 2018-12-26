from flask import Flask, request,jsonify
from flask_restful import Resource, Api
# DO THIS FIRST:
# pip install -r requirements.txt
# python3 api.py

app = Flask(__name__)
api = Api(app)

class People(Resource):
    def get(self):
        # return a list of people dictinary as json:
        return jsonify([{"people":{"name":"Joe"}}])
    def post(self):
        return "created"
    def put(self):
        return "updated"
    def delete(self):
        return "delted"

api.add_resource(People,'/people')

if __name__=="__main__":
    app.run(debug=True)

# pip freeze > requirements.txt

# pip install pipreqs
# pipreqs .
