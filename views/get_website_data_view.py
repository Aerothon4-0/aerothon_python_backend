
from flask import current_app as app
from flask import Flask, jsonify,request

import logging
import json 
import uuid

from models.models import Website,database

def get_website_data():
	if request.method == 'GET':
		
		try:
			function_uuid = uuid.uuid1() 
			function_name = 'Get website'

			#get data
			try:
				website_name = request.args.get('app','')
				token = request.args.get('token','')
				print(website_name , "website_name")
				print(token , "token")

			except Exception as e:
				print(e)
				raise Exception("error in get data")

			#get data from database
			try:
				website_obj = Website.query.filter_by(
					website_name=website_name,
					token = token
					).first()

				data = {}
				data['website_name'] = website_obj.website_name
				data['company_name'] = website_obj.company_name
				data['company_description'] = website_obj.company_description
				data['backend_port'] = website_obj.backend_port
				data['frontend_port'] = website_obj.frontend_port
				data['frontend_url'] = website_obj.frontend_url
				data['backend_url'] = website_obj.backend_url

				
				print(data , "data")
				
			except Exception as e:
				print(e)
				raise Exception("data not found")

			#error in generate data
			

		except Exception as e:
			print(e)
			return jsonify({
				'error':'true',
				'message': str(e),
				'function_name':function_name,
				'function_uuid':function_uuid,
			})


		return jsonify({
				'error':'false',
				'message':'success',
				'function_name':function_name,
				'function_uuid':function_uuid,
				'response_data':data
			})


