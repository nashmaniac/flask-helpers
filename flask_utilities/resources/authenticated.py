from flask_restplus import Resource
from flask_jwt_extended import jwt_required


class AuthenticatedResource(Resource):
    decorators = [jwt_required]
