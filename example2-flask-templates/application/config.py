from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    ENV = os.getenv('ENV')
    DEBUG = os.getenv('DEBUG')
