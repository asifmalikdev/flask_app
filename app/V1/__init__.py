from flask import Blueprint
from flask_restx import Api
from .resources.user_info import user_ns
from .models.user_schema import register_user_models

def create_app_v1():
    v1_blueprint = Blueprint("v1_blueprint", __name__)

    api_v1 = Api(v1_blueprint, title="User API", version="1.0")

    register_user_models(user_ns)

    api_v1.add_namespace(user_ns)

    return v1_blueprint
