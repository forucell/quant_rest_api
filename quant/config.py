# Default configuration

import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
JSON_AS_ASCII = False

USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
DBNAME=os.getenv("DBNAME")



