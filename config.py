import os

class Config(object):
    SECRET_KEY = 'm1y2s3e4c5r6e7t8k9e0y'

class DevelopmentConfig_local(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://elrogerrr:0p9o8i7u6y5t@localhost/db_ifglobal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig_ionos(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://elrogerrr:0p9o8i7u6y5t@162.255.87.205/db_ifglobal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig_sqlite(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/db_ifglobal.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False