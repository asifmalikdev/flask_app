import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret123")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 1

    REDIS_URL = "redis://redis:6379/0"
 

# class DevelopmentConfig(Config):
#     DEBUG = True

# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  

# class ProductionConfig(Config):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/dbname'  