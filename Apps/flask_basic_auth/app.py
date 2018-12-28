from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "johnpassword",
    "susan": "susanpassword"
}

@auth.get_password
def get_pw(username):
    #If the user exists in the dictionary of users...
    if username in users:
        #..return the password of the user.
        return users.get(username)
    #The returned password will get passed to the auth.get_password() decorator as the pasword for the user.
    return None

@app.route('/')
@auth.login_required #Require login at this endpoint
def index():
    return "Hello, {}!".format(auth.username()) #Not sure where .username()comes from

if __name__ == '__main__':
    app.run()