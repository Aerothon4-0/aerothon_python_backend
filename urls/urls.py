from flask import current_app as app
from flask import Blueprint

from views.views import generate_website
from views.get_website_data_view import get_website_data
from views.callchatbot import chat_response_message

urls = Blueprint('aerothon', __name__)

# save
urls.add_url_rule('/code/generate_website', 'generate_website', generate_website, methods=['POST'])
urls.add_url_rule('/code/get_website_data', 'get_website_data', get_website_data, methods=['GET'])
urls.add_url_rule('/code/chatbotreply', 'chat_response_message', chat_response_message, methods=['POST'])

