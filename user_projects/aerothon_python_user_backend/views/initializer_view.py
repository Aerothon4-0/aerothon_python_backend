
import os
import requests

from models.models import Website,database
from settings import *

def initializ_data():
	#save data
	print("--start initializ data--")
	try:
		app_name = os.environ.get('APP','Alans')
		token = os.environ.get('TOKEN','40b1abb5db2011ecb95ec809a8853d3d')

		PARAMS = {
			'app':app_name,
			'token':token,
			}

		response = requests.get(url = MAIN_BACKEND_SERVER_URL, params = PARAMS)
		data = response.json()

		print(data , "data")
	except Exception as e:
		print(e)

	#save data
	try:
		website_obj = Website(
			token=token,

			website_name=data['response_data']['website_name'], 
			company_name=data['response_data']['company_name'],
			company_description=data['response_data']['company_description'],

			status = 'active'

		)
		database.session.add(website_obj)
		database.session.commit()
	except Exception as e:
		print(e)

	print("--end initializ data--")
