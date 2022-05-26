from flask import current_app as app
from flask import Blueprint

from views.views import get_company_details


urls = Blueprint('aerothon_user', __name__)

# save
urls.add_url_rule('/user/get_data', 'get_company_details', get_company_details, methods=['GET'])

