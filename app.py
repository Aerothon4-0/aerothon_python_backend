
from flask import Flask, jsonify,request
# from flask_sqlalchemy import SQLAlchemy
import os
import click
import logging

from flask_migrate import Migrate

from urls.urls import urls
from models.models import database
from flask_cors import CORS

# from settings import *



app = Flask(__name__)

logging.basicConfig(filename="logs/error.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


print("In app launch")
app.register_blueprint(urls)

CORS(app)

def page_not_found(e):
  return jsonify(message='Thanku'), 200

app.register_error_handler(404, page_not_found)

database.init_app(app)
migrate = Migrate(app, database)


if __name__ == '__main__':
	app.run()



