from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

import enum

database = SQLAlchemy()



class TechnologyEnum(enum.Enum):
    python = 1
    node = 2
    react = 3
    angular = 4
    react_native = 5


class Website(database.Model):
	__tablename__ = 'website_details'
	
	id = database.Column(database.Integer , primary_key=True, autoincrement=True)
	token = database.Column(database.String(1450)  , nullable=False)
	backend_port = database.Column(database.Integer , nullable=True)
	frontend_port = database.Column(database.Integer , nullable=True)

	website_name = database.Column(database.String(36)  , nullable=False)
	company_name = database.Column(database.String(36)  , nullable=False)
	company_description = database.Column(database.String(1450)  , nullable=False)

	is_front_end = database.Column(database.Boolean, default=False, nullable=False)
	front_end = database.Column(database.Enum(TechnologyEnum), default=TechnologyEnum.react,nullable=False)
	front_type = database.Column(database.String(36)  , nullable=False)

	is_back_end = database.Column(database.Boolean, default=False, nullable=False)
	back_end = database.Column(database.Enum(TechnologyEnum), default=TechnologyEnum.python,nullable=False)

	is_mobile_app_end = database.Column(database.Boolean, default=False, nullable=False)
	mobile_app = database.Column(database.Enum(TechnologyEnum), default=TechnologyEnum.react_native,nullable=False)

	frontend_url = database.Column(database.String(1450)  , nullable=True)
	backend_url = database.Column(database.String(1450)  , nullable=True)

	created_at = database.Column(database.DateTime, nullable=False,default=datetime.utcnow)
	updated_at = database.Column(database.DateTime, nullable=False,default=datetime.utcnow)
