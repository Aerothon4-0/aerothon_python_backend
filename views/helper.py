from flask import current_app as app
from flask import Flask, jsonify,request

import subprocess
import sys
import getopt

from settings import * 


def create_python_backend_website(website_name,token,port):
	try:
		print("--before start docker--")
		bashCommand = 'sudo python {}/start.py -a "python_backend" -p {} -e {} --token {} -t create'.format(USER_BACKEND_PROJECT_DIR,port,website_name,token)
		output = subprocess.check_output(['bash','-c', bashCommand],cwd=USER_BACKEND_PROJECT_DIR)
		print("--after start docker--")
	except Exception as e:
		print(e)
		app.logger.error('ERROR : %s ',str(e) )

	backend_url = "http://0.0.0.0:{}{}".format(port,PYTHON_USER_BACKEND_END_POINT)

	return backend_url

