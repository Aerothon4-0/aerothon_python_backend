from flask import current_app as app
from flask import Blueprint

from views.views import generate_website


urls = Blueprint('aerothon', __name__)

# save
urls.add_url_rule('/code/generate_website', 'generate_website', generate_website, methods=['POST'])

