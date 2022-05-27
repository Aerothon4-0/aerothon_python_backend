
from flask import current_app as app
from flask import Flask, jsonify,request

import logging
import json 
import uuid

from models.models import Website,database


def get_company_details():
	if request.method == 'GET':
		
		try:
			function_uuid = uuid.uuid1() 
			function_name = 'Get website details'
			data = {}
			#get data
			try:
				website_name = request.args.get('app','')
				token = request.args.get('token','')
				print(website_name , "website_name")
				print(token , "token")

			except Exception as e:
				print(e)
				app.logger.error('ERROR : %s ',str(e) )
				raise Exception("error in get data")


			#get data from database
			try:
				website_obj = Website.query.first()
				# website_obj = Website.query.filter_by(
				# 	website_name=website_name,
				# 	token = token
				# 	).first()

				data = {}
				data['website_name'] = website_obj.website_name
				data['company_name'] = website_obj.company_name
				data['company_description'] = website_obj.company_description

				
				print(data , "data")
				
			except Exception as e:
				print(e)
				app.logger.error('ERROR : %s ',str(e) )
				raise Exception("data not found")


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


