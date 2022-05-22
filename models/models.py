from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


database = SQLAlchemy()

class Website(database.Model):
	__tablename__ = 'website_details'
	
	id = database.Column(database.Integer , primary_key=True, autoincrement=True)

	website_name = database.Column(database.String(36)  , nullable=False)
	company_name = database.Column(database.String(36)  , nullable=False)
	company_description = database.Column(database.String(1450)  , nullable=False)
	created_at = database.Column(database.DateTime, nullable=False,default=datetime.utcnow)
	updated_at = database.Column(database.DateTime, nullable=False,default=datetime.utcnow)
