from flask import Flask
from flask_cors import CORS
import json
from environs import Env


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

env = Env()
ENV = env.str("ENV")



from billing.billing_service import billing_routes
