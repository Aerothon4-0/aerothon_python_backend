
from flask import Flask, jsonify,request
# from flask_sqlalchemy import SQLAlchemy
import os
import click
import logging

from flask_migrate import Migrate

from urls.urls import urls
from models.models import database

from views.initializer_view import initializ_data

# from settings import *



application = Flask(__name__)

logging.basicConfig(filename="logs/error.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


application.debug = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


print("In app launch")
application.register_blueprint(urls)

def page_not_found(e):
  return jsonify(message='message') , 200

application.register_error_handler(404, page_not_found)

database.init_app(application)
migrate = Migrate(application, database)

@application.cli.command("initialize-data")
def initialize_data():
	initializ_data()

if __name__ == '__main__':
	application.run()
	



