class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'very secret key'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
