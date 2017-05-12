# coding:utf-8
__author__ = "piels"


class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:19910203@127.0.0.1:3306/blog_db"
