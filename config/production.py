from . import Config
import os

class Production(Config):

    ENV_TYPE = "Production" 

    DB_NAME = "dei9hiiejp9lcl"
    DB_USER = "uygbizvsfjuwas"
    DB_PASSWORD = "487e70d4254d0b11e6be357ddcf8d6a38aa10bedc19fe0499950c6434bc22a62"
    DB_HOST = "ec2-174-129-226-232.compute-1.amazonaws.com"
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    username = "Aleksa"
    password = "123456"