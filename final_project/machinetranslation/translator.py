""" docstring making ibm connection"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('rBCqHlw7_QFLKnegAQk39a0hc99BNBNJ5nN7ZtSaycnA')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/946e95d1-0aad-439a-9a8c-91ee7bba1dc5')
def english_to_french(english_text):
    """Englosh to French"""
    translation = language_translator.translate(text = english_text, model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """French to English"""
    translation = language_translator.translate(text = french_text, model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
