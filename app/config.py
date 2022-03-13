#imports
import os

class Config:
    
    #Secret Key configuration and Database location
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    
class ProdConfig(Config):
    
    #Development Database Configuration 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    DEBUG = True
    
    
#Different Config Options
config_options = {
'development':DevConfig,
'production':ProdConfig
}