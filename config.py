#


class BaseConfig(object):
    DEBUG = True


class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True
