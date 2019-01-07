from flask import Flask
app = Flask(__name__)

from .backend.controllers import *
from .frontend.routes import *

