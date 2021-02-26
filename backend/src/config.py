from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    PROPAGATE_EXCEPTIONS = True
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_SECRET_KEY=environ.get('JWT_SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False
    JWT_COOKIE_SECURE = True


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    JWT_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True