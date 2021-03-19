from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    ENV = os.getenv('ENV', 'production')
    FLASK_STATIC_DIGEST_HOST_URL = os.getenv('FLASK_STATIC_DIGEST_HOST_URL', '')
    DEBUG = True if os.getenv('DEBUG') == 'True' else False
