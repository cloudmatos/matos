from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from api.route.home import home_api
from api.route.resource import resource_api
from config.exceptions import (
    ItemNotFoundException,
    UnauthorizedException,
    ForbiddenException,
    ServerErrorException,
    InvalidDataException,
    BadRequestException
)
from utils.log import config_logger


def create_app():
    """Create app"""
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Matos API Starter Kit',
    }
    Swagger(app)
    CORS(app)
    ## Initialize Config
    config_logger()
    app.config.from_pyfile('environment.py')
    app.register_blueprint(home_api, url_prefix='/api')
    app.register_blueprint(resource_api, url_prefix='/resources')
    register_errorhandlers(app)
    return app


def register_errorhandlers(app):
    """register custom error handler"""
    def error_handler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(ItemNotFoundException)(error_handler)
    app.errorhandler(UnauthorizedException)(error_handler)
    app.errorhandler(ForbiddenException)(error_handler)
    app.errorhandler(ServerErrorException)(error_handler)
    app.errorhandler(InvalidDataException)(error_handler)
    app.errorhandler(BadRequestException)(error_handler)
