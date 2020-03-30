from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URL') or f'sqlite:///{path.join(basedir, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = int(environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    ADMINS = [environ.get('ADMIN')]
    POSTS_PER_PAGE = 1
    LANGUAGES = ['en', 'es']