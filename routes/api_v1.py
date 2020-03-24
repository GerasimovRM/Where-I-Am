from flask import Blueprint
from flask_restful import Api
from resources.user import UserResource
from resources.user_list import UserListResource

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(UserListResource, '/user')
api.add_resource(UserResource, '/user/<int:user_id>')

