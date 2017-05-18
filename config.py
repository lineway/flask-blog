# coding:utf-8
__author__ = "piels"


class Config(object):
    SECRET_KEY = '40ee3838e2f45a494484d869d2acd24804d44835135b10e54456c8afd1d75eb2'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:19910203@127.0.0.1:3306/blog_db"
