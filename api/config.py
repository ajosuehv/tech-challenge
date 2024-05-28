from api.utils import get_env_variable
from dotenv import load_dotenv
import os
load_dotenv('env/db.dotenv')


POSTGRES_URL = os.environ['POSTGRES_URL']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_PORT = os.environ['POSTGRES_PORT']

class Config(object):
    SQLALCHEMY_DATABASE_URI = (f"postgresql://"
          f"{POSTGRES_USER}"
          f":{POSTGRES_PASSWORD}"
          f"@{POSTGRES_URL}"
          f":{POSTGRES_PORT}"
          f"/{POSTGRES_DB}")
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False