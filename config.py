import os
from dotenv import load_dotenv


# import enviromental variables 
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")


class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLAlchemy_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = SECRET_KEY



