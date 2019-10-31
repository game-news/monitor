import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'as32ugcFUY434iA33aSFuGgs')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    JSON_AS_ASCII = False
    DSN = os.getenv('DSN')

    MONGODB_SETTINGS = {
        'db': 'spider',
        'host': os.getenv('MONGO_URI')
    }

    MONGO_URI = os.getenv('MONGO_URI')
    print(MONGO_URI)

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.db')


class ProductionConfig(BaseConfig):
    FLASK_DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
