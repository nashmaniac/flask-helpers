from flask import abort
from flask_restplus import fields

from flask_utilities.fields import Email


class CustomValidator(object):
    @classmethod
    def validate_payload(cls, payload, api_model):
        for key in api_model:
            if api_model[key].required and key not in payload:
                abort(400, 'Required field \'%s\' missing' % key)
            # check payload
        for key in payload:
            field = api_model[key]
            if isinstance(field, fields.List):
                field = field.container
                data = payload[key]
            else:
                data = [payload[key]]
            if isinstance(field, Email) and hasattr(field, 'validate'):
                for i in data:
                    if not field.validate(i):
                        abort(400, 'Validation of \'%s\' field failed' % key)
