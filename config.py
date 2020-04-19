#Define app directory
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
        
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
