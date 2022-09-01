from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.welcome import WelcomeModel
from api.schema.welcome import WelcomeSchema

home_api = Blueprint('api', __name__)


@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeSchema
        }
    }
})
def welcome():
    """
    Welcome to Matos.
    """
    result = WelcomeModel()
    return WelcomeSchema().dump(result), 200
