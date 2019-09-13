from flask_restplus.fields import String
from validate_email import validate_email


class Email(String):
    __schema_example__ = "shetu@domain.com"
    def validate(self, value):
        return validate_email(value)
