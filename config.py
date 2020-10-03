import os
import cloudinary

class Config:
    '''
        General configuration parent class
    '''
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:g11111111@localhost/books'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # cloudinary configuration
    cloudinary.config(cloud_name='group6flask', api_key='771748118468722',
                      api_secret='Uye0Bi1UGZRvFNO8O8viekFqqIE')

    #  email configurations
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'mwalonick@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    '''
        Development  configuration child class

        Args:
            Config: The parent configuration class with General configuration settings
        '''
    DEBUG = True


class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    '''
        Production  configuration child class

        Args:
            Config: The parent configuration class with General configuration settings


        '''
    DEBUG = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig,
}