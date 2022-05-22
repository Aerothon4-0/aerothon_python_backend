
from flask import current_app as app
from flask import Flask, jsonify,request

import logging
import json 
import uuid

from models.models import Website,database

def generate_website():
	if request.method == 'POST':
		
		try:
			function_uuid = uuid.uuid1() 
			function_name = 'Generate website'

			try:		
				data = json.loads(request.data)
			except Exception as e:
				print(e)
				raise Exception("data not found")
			
			Website_obj = Website(website_name='john', company_name='doe',
                       company_description='jd@example.com')
			database.session.add(Website_obj)
			database.session.commit()


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
				'response_data':{}
			})


