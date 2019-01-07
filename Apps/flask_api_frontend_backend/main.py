from app import app
from flask import jsonify

@app.route('/ping', methods=['GET'])
def dummy_endpoint():
    """ Testing endpoint """
    return jsonify({'data': 'Server running'}), 200

if __name__ == '__main__':
    app.run(debug=True)

