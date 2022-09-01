from http import HTTPStatus
import traceback
from flask import Blueprint
from flasgger import swag_from
from api.schema.resource import ResourceSchema
from api.model.resource import ResourceModel
from services.resource_service import ResourceService
from config.exceptions import BadRequestException


resource_api = Blueprint('resources', __name__)


@resource_api.route('/<provider>')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Fetch cloud resources from service account file',
            'schema': ResourceSchema
        }
    }
})
def fetchResources(provider):
    """
    Fetch resources and metadata using cloud API's in real time.
    ---
    parameters:
      - name: provider
        in: path
        type: string
        enum: ['gcp', 'aws', 'azure']
        required: true
        default: gcp
    """
    try:
        resource_service_obj = ResourceService(provider)
        pretty_resources, _ = resource_service_obj.get_resource()
    except Exception as ex:
        traceback.print_exc()
        raise BadRequestException(message=str(ex)) from ex

    return ResourceSchema().dump(ResourceModel(pretty_resources)), 200
