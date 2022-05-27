from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

import enum

database = SQLAlchemy()



class Website(database.Model):
	__tablename__ = 'website_details'
	
	id = database.Column(database.Integer , primary_key=True, autoincrement=True)
	token = database.Column(database.String(1450)  , nullable=False)

	website_name = database.Column(database.String(36)  , nullable=False)
	company_name = database.Column(database.String(36)  , nullable=False)
	company_description = database.Column(database.String(1450)  , nullable=False)

	status = database.Column(database.String(36)  , nullable=False) # active , deactive

	created_at = database.Column(database.DateTime, nullable=False,default=datetime.utcnow)
	updated_at = database.Column(database.DateTime, nullable=False,default=datetime.utcnow)




class Bulb(database.Model):
	__tablename__ = 'buld_iot'
	
	id = database.Column(database.Integer , primary_key=True, autoincrement=True)
	bulb_status = database.Column(database.Boolean, default=False, nullable=False)
	