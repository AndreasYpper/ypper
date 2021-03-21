import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

#config file with default configurations
from config import *

from resources.user import (
    User,
    UserLogin,
    UserLogout,
    UserRegister
)
from resources.machine import Machine, Machines

app = Flask(__name__)

#cors setup
cors = CORS(app, resources={r"*": {"origins": "*", "supports_credentials": True}})

#jwt setup
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_COOKIE_PATH"] = "/api/"
app.config["JWT_REFRESH_COOKIE_PATH"] = "/token/refresh"
app.config.from_object(os.environ.get("APP_SETTINGS"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
api = Api(app)

jwt = JWTManager(app)

from db import db


#api endpoints


if __name__ == "__main__":
    if os.environ.get("APP_SETTINGS") == "config.DevelopmentConfig":
        app.run(host="localhost")
    else:
        app.run(host="0.0.0.0")