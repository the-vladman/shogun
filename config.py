#
import os
import logging

class BaseConfig(object):
    DEBUG = True
    LEVEL = logging.DEBUG



class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "garlic"
    USER = "dog"
    PASSWORD = "easy"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/users.db'
    LEVEL = logging.DEBUG

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/users.db'
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')
    LEVEL = logging.INFO
