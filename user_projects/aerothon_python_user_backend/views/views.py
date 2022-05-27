
from flask import current_app as app
from flask import Flask, jsonify,request

import logging
import json 
import uuid

from models.models import Website,Bulb,database


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






def update_bulb_status():
	if request.method == 'GET':
		
		try:
			function_uuid = uuid.uuid1() 
			function_name = 'Get bulb status'
			data = {}
			#get data

			#get data from database
			try:
				bulb = Bulb.query.first()
				data = {}
				data['bulb_status'] = bulb.bulb_status
				print(data , "data")
				
			except Exception as e:
				print("Bulb not found. Create one")
				bulb_obj = Bulb(
						bulb_status=True
					)
				database.session.add(bulb_obj)
				database.session.commit()
				data = {}
				data['bulb_status'] = True

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
	elif request.method == 'POST':
		function_uuid = uuid.uuid1() 
		function_name = 'update bulb status'
		data = {}
		#get data
		try:
			input_data = json.loads(request.data)
			bulb_status = input_data.get('bulb_status',False)
			print(bulb_status , "bulb_status")

		except Exception as e:
			print(e)
			app.logger.error('ERROR : %s ',str(e) )


		#get data from database
		try:
			bulb_obj = Bulb.query.first()
			bulb_obj.bulb_status = bulb_status
			database.session.commit()
		except Exception as e:
			print(e)


		return jsonify({
				'error':'false',
				'message':'success',
				'function_name':function_name,
				'function_uuid':function_uuid,
			})