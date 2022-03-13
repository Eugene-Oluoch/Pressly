#imports
import os

class Config:
    
    #Secret Key configuration and Database location
    SECRET_KEY = 'dcadb4817ccfc31f2a0b'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://crabs:Greenland@localhost/pressly'
    
    
class ProdConfig(Config):
    
    #Development Database Configuration 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://crabs:Greenland@localhost/5433/pressly'


class DevConfig(Config):
    DEBUG = True
    
    
#Different Config Options
config_options = {
'development':DevConfig,
'production':ProdConfig
}