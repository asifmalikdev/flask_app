from flask import Flask
from .V1 import create_app_v1
from .extentions import db, cache
from flask_migrate import Migrate
from .redis_app import redis_app    

migrate = Migrate()

def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    cache.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(create_app_v1(), url_prefix='/api/v1')
    redis_app.init_app(app)

    return app
