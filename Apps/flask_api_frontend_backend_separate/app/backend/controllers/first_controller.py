from app import app
from flask import jsonify

#API CODE GOES HERE

@app.route('/api/v1/controller1')
def controller1():
    return jsonify({"msg":"hello"})