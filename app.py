
from flask import Flask, jsonify,request
# from flask_sqlalchemy import SQLAlchemy
import os
import click
import logging
import json
from flask_migrate import Migrate
from flask_cors import CORS
from requests import get 
from urls.urls import urls
from models.models import database
import subprocess

# from settings import *



application = Flask(__name__)
cors = CORS(application)
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
  return jsonify(message='Thanku'), 200

application.register_error_handler(404, page_not_found)

database.init_app(application)
migrate = Migrate(application, database)

@application.route('/code/generate_website',methods=['POST']) 
def generate_website(): 
  if request.method=='POST': 
    result  = json.loads(request.data.decode("utf-8"))
    print(result)
    # save data received in DB 
    #
    # create docker for backend 
    cmd = "python start.py -a '"+result['back_end']+"_backend' -p Alans --token 40b1abb5db2011ecb95ec809a8853d3d -t create"
    #sudo python start.py -a "python_backend" -p 5001 -e Alans --token 40b1abb5db2011ecb95ec809a8853d3d -t create
    subprocess.Popen(cmd, shell=True)
    # receive user backend url
    #
    # docker for frontend by passing the backend url
    #
  else:
    print("error")
    return jsonify(isError= True,
                    message= "Failed",
                    statusCode= 400)
  return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200)
                    #data= data), 200

@application.route('/code/get_data',methods=['GET']) 
def get_website_data(): 
  if request.method=='GET': 
    #fetch URL of user backend and token
    #data = get_website_data_view()
    print("data")
    data = {}
    #data = {"url":"http://0.0.0.0:5001/code/website_data","website_name":"abc","company_name":"abc","description":"the abc company","frontend":"react","isbackend":"True","backend":"Python"}

  else:
    print("error")
    return jsonify(isError= True,
                    message= "Failed",
                    statusCode= 400)
  return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200,
                    data= data) #200


if __name__ == '__main__':
	application.run()



