class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'very secret key'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+mysqldb://root:kinglion@localhost:3306/jobplus?charset=utf8'
