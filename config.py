import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config:
    MAIL_USE_TLS = True

    if os.environ.get('FLASK_ENV'):
        FLASK_ENV = os.environ.get('FLASK_ENV')
    else:
        FLASK_ENV = 'FLASK_ENV_VAR_NOT_SET'

    # SQLAlchemy configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        SQLALCHEMY_DATABASE_URI = 'DATABASE_URL_ENV_VAR_NOT_SET'

    # Celery configuration
    if os.environ.get('CELERY_BROKER_URL'):
        CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    else:
        CELERY_BROKER_URL = 'CELERY_BROKER_URL_ENV_VAR_NOT_SET'

    if os.environ.get('RESULT_BACKEND'):
        RESULT_BACKEND = os.environ.get('RESULT_BACKEND')
    else:
        RESULT_BACKEND = 'RESULT_BACKEND_ENV_VAR_NOT_SET'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class QAConfig(Config):
    SSL_DISABLE = (os.environ.get('SSL_DISABLE') or 'True') == 'True'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    SSL_DISABLE = (os.environ.get('SSL_DISABLE') or 'True') == 'True'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'qa': QAConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
