
from flask import current_app as app
from flask import Flask, jsonify,request

import logging
import json 
import uuid

from models.models import Website,database
from .helper import create_python_backend_website,create_react_website

def generate_website():
	if request.method == 'POST':
		
		try:
			function_uuid = uuid.uuid1() 
			function_name = 'Generate website'
			response_data = {}

			backend_start_port = 5000
			frontend_start_port = 3000

			try:		
				data = json.loads(request.data)
			except Exception as e:
				print(e)
				app.logger.error('ERROR : %s ',str(e) )
				raise Exception("data not found")
			
			#get data
			try:
				website_name = data.get('website_name','default_website')
				company_name = data.get('company_name','default_cmpny')
				company_desc = data.get('company_description','default')
				
				is_front_end = data.get('is_front_end',True)
				front_end = data.get('front_end','react')
				front_type = data.get('front_type','blog')

				is_back_end = data.get('is_back_end',True)
				back_end = data.get('back_end','python')

				is_mobile_app_end = data.get('is_mobile_app_end',False)
				mobile_app = data.get('mobile_app','react_native')

				token = str( uuid.uuid1().hex  )
				print(token , "token")
				
			except Exception as e:
				print(e)
				app.logger.error('ERROR : %s ',str(e) )
				raise Exception("error in get data")

			#save data
			try:
				website_obj = Website(
					token=token,

					website_name=website_name, 
					company_name=company_name,
	                company_description=company_desc,

	                is_front_end=is_front_end,
	                front_end=front_end,
	                front_type=front_type,

	                is_back_end=is_back_end,
	                back_end=back_end,

	                is_mobile_app_end=is_front_end,
	                mobile_app=mobile_app


	                )
				database.session.add(website_obj)
				database.session.commit()
			except Exception as e:
				print(e)
				app.logger.error('ERROR : %s ',str(e) )
				raise Exception("error in save data")

			#error in generate data
			try:
				website_obj = Website.query.filter_by(
					website_name=website_name,
					token = token
					).first()
				obj_id = website_obj.id

				back_end_port = backend_start_port + obj_id
				front_end_port = frontend_start_port + obj_id
				print(back_end_port , "back_end_port")
				print(front_end_port , "front_end_port")

				backend_url = ''
				frontend_url = ''
				if back_end == 'python':
					backend_url = create_python_backend_website(website_name,token,back_end_port)

				if front_end == 'react':
					frontend_url = create_react_website(website_name,token,front_end_port,front_type)
				



				response_data['backend_url'] = backend_url
				response_data['frontend_url'] = frontend_url

				website_obj.backend_port = back_end_port
				website_obj.frontend_port = front_end_port

				website_obj.backend_url = backend_url
				website_obj.frontend_url = frontend_url
				# database.session.add(website_obj)
				database.session.commit()

			except Exception as e:
				print(e)
				app.logger.error('ERROR : %s ',str(e) )
				raise Exception("error in generate url")


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
				'response_data':response_data
			})


