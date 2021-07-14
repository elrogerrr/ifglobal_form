import os

class Config(object):
    SECRET_KEY = 'm1y2s3e4c5r6e7t8k9e0y'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://elrogerrr:0p9o8i7u6y5t@162.255.87.205/db_ifglobal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False