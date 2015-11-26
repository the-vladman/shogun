#


class BaseConfig(object):
    DEBUG = True


class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SECRET_KEY = "garlic"
    USER = "dog"
    PASSWORD = "easy"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/users.db'
