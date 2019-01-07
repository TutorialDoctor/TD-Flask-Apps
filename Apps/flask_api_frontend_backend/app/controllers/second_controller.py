from app import app
from flask import jsonify

#API CODE GOES HERE

@app.route('/api/v1/controller2')
def controller2():
    return jsonify({"msg":"hello 2"})