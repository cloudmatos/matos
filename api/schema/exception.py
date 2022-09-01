from flask_marshmallow import Schema
from marshmallow.fields import Str, Int


class ExceptionSchema(Schema):
    class Meta:
        fields = ['message', 'status']

    message = Str()
    status = Int()
