from flask import current_app as app
from flask import Flask, jsonify,request

import subprocess
import sys
import getopt

from settings import * 


def create_python_backend_website(website_name,token,port):
	try:
		name = "python_backend_{}".format(str(port))
		print("--before start backend docker--")
		bashCommand = 'python {}/start.py -a "{}" -p {} -e {} --token {} -t create'.format(USER_BACKEND_PROJECT_DIR,name,port,website_name,token)
		output = subprocess.check_output(['bash','-c', bashCommand],cwd=USER_BACKEND_PROJECT_DIR)
		print("--after start backend docker--")
		app.logger.info('INFO : %s ',str(output) )
	except Exception as e:
		print(e)
		app.logger.error('ERROR : %s ',str(e) )

	backend_url = "{}:{}{}".format(SERVER_IP_ADDRESS,port,PYTHON_USER_BACKEND_END_POINT)

	return backend_url


def create_react_website(website_name,token,port,front_type):
	try:
		project_dir = FRONT_END_PROJECT_DIR[front_type] if front_type in FRONT_END_PROJECT_DIR.keys() else ""
	except:
		pass 

	try:
		name = "react_docker_{}".format(str(port))
		print("--before start frontend docker--")
		bashCommand = 'python {}/start.py -a "{}" -p {} -e {} --token {} -t create'.format(project_dir,name,port,website_name,token)
		output = subprocess.check_output(['bash','-c', bashCommand],cwd=project_dir)
		print("--after start frontend docker--")
		app.logger.info('INFO : %s ',str(output) )
	except Exception as e:
		print(e)
		app.logger.error('ERROR : %s ',str(e) )

	backend_url = "{}:{}".format(SERVER_IP_ADDRESS,port)

	return backend_url
